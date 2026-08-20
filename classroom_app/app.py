import os

import streamlit as st

from classroom import Classroom

st.set_page_config(page_title="Smart Class", layout="wide", initial_sidebar_state="expanded")


@st.cache_resource
def get_classroom():
    return Classroom()


def load_style():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.css")
    with open(path) as file:
        st.html(f"<style>{file.read()}</style>")


def panel_title(text):
    st.html(f"<div class='panel-title'>{text}</div>")


room = get_classroom()


def sidebar_login():
    st.sidebar.title("Smart Class")
    role = st.sidebar.radio("I am a", ["Student", "Teacher"])
    name = st.sidebar.text_input("Name")
    code = st.sidebar.text_input("Lesson code")
    password = st.sidebar.text_input("Password", type="password") if role == "Teacher" else ""

    if st.sidebar.button("Enter", type="primary", width="stretch"):
        if not name or not code.isdigit():
            st.sidebar.error("Enter a name and a numeric lesson code.")
        else:
            st.session_state.role = role
            st.session_state.name = name
            st.session_state.code = int(code)
            st.session_state.password = password
            st.rerun()

    if st.session_state.get("role"):
        st.sidebar.divider()
        st.sidebar.caption(f"Connected as {st.session_state.name}")
        if st.sidebar.button("Leave", width="stretch"):
            for key in ["role", "name", "code", "password"]:
                st.session_state.pop(key, None)
            st.rerun()


def lesson_header(lesson):
    with st.container(border=True):
        left, right = st.columns([3, 1], vertical_alignment="center")
        left.markdown(f"## {lesson.lesson_name}")
        left.caption(f"Lesson code {lesson.lesson_code}")
        right.metric("Time left", lesson.get_formatted_time())


def create_lesson_form():
    with st.container(border=True):
        panel_title("Open a lesson")
        st.caption("No active lesson with this code yet.")
        with st.form("new_lesson"):
            lesson_name = st.text_input("Lesson name")
            duration = st.number_input("Duration in minutes", min_value=5, max_value=300, value=45, step=5)
            if st.form_submit_button("Open lesson", type="primary"):
                if lesson_name:
                    room.open_lesson(
                        st.session_state.name,
                        st.session_state.password,
                        st.session_state.code,
                        lesson_name,
                        int(duration),
                    )
                    st.rerun()
                else:
                    st.error("Lesson name is required.")


def teacher_page():
    lesson = room.get_lesson(st.session_state.code)
    if not lesson:
        create_lesson_form()
        return

    teacher = room.get_teacher(st.session_state.name, st.session_state.password, lesson.lesson_code)
    lesson_header(lesson)

    materials, classroom_side = st.columns(2)

    with materials:
        with st.container(border=True):
            panel_title("Class material")
            with st.form("add_link", clear_on_submit=True):
                link = st.text_input("Link to a task or a file", placeholder="https://")
                if st.form_submit_button("Add", type="primary") and link:
                    room.add_link(teacher, lesson, link)

            if lesson.lesson_appendices:
                for index, appendix in enumerate(lesson.lesson_appendices, 1):
                    st.markdown(f"{index}. [{appendix}]({appendix})")
            else:
                st.caption("No material added yet.")

    with classroom_side:
        help_queue(teacher, lesson)


@st.fragment(run_every="3s")
def help_queue(teacher, lesson):
    with st.container(border=True):
        panel_title("Help requests")

        waiting = teacher.get_help_queue(lesson)
        if waiting:
            for student in waiting:
                line, button = st.columns([3, 1], vertical_alignment="center")
                line.warning(f"{student.name} is asking for help")
                if button.button("Accept", key=f"accept_{student.name}", type="primary"):
                    room.accept_help(teacher, lesson, student)
                    st.rerun(scope="fragment")
        else:
            st.caption("Nobody is waiting for help.")

        open_rooms = [s for s in lesson.students if room.get_room(lesson, s.name)]
        if open_rooms:
            st.divider()
            panel_title("Open calls")
            for student in open_rooms:
                line, button = st.columns([3, 1], vertical_alignment="center")
                line.link_button(f"Join call with {student.name}", room.get_room(lesson, student.name), width="stretch")
                if button.button("End", key=f"end_{student.name}"):
                    room.close_room(lesson, student.name)
                    st.rerun(scope="fragment")

    with st.container(border=True):
        panel_title(f"Students ({len(lesson.students)})")
        if lesson.students:
            for student in lesson.students:
                st.markdown(f"- {student.name}")
        else:
            st.caption("No students joined yet.")


def student_page():
    lesson = room.get_lesson(st.session_state.code)
    if not lesson or not lesson.is_active():
        st.error("This lesson does not exist or has already ended.")
        return

    student = room.join(st.session_state.name, lesson)
    lesson_header(lesson)

    tasks, help_side = st.columns([2, 1])

    with tasks:
        with st.container(border=True):
            panel_title("My tasks")
            if lesson.lesson_appendices:
                done = st.session_state.setdefault("done", set())
                for index, appendix in enumerate(lesson.lesson_appendices):
                    checked = st.checkbox(f"[{appendix}]({appendix})", key=f"task_{index}", value=index in done)
                    if checked:
                        done.add(index)
                    else:
                        done.discard(index)
                st.divider()
                st.progress(len(done) / len(lesson.lesson_appendices))
                st.caption(f"{len(done)} of {len(lesson.lesson_appendices)} tasks completed")
            else:
                st.caption("The teacher has not added any material yet.")

    with help_side:
        help_panel(student, lesson)


@st.fragment(run_every="3s")
def help_panel(student, lesson):
    with st.container(border=True):
        panel_title("Need help?")

        url = room.get_room(lesson, student.name)
        if url:
            st.success("The teacher opened a private room for you.")
            st.link_button("Join the call", url, type="primary", width="stretch")
            if st.button("I am done", width="stretch"):
                room.close_room(lesson, student.name)
                st.rerun(scope="fragment")
        elif student.need_help:
            st.info("Your request was sent. Waiting for the teacher.")
            if st.button("Cancel request", width="stretch"):
                student.cancel_help_request()
                st.rerun(scope="fragment")
        else:
            st.caption("Only you and the teacher join the room, nobody else sees you.")
            if st.button("Ask teacher", type="primary", width="stretch"):
                student.request_help()
                st.rerun(scope="fragment")


load_style()
sidebar_login()

if not st.session_state.get("role"):
    st.title("Smart Class")
    st.write("Join a lesson from the side panel to see your tasks and to talk with the teacher one on one.")
elif st.session_state.role == "Teacher":
    teacher_page()
else:
    student_page()
