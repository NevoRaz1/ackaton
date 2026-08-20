import os
import sys

LOGIC_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ackaton")
if LOGIC_PATH not in sys.path:
    sys.path.insert(0, LOGIC_PATH)

from Lesson import Lesson
from Student import Student
from Teacher import Teacher
from call_link import create_room_url


def load_database():
    try:
        import database
        database.init_db()
        return database
    except Exception:
        return None


class Classroom:
    def __init__(self):
        self.db = load_database()
        self.lessons = {}
        self.teachers = {}
        self.rooms = {}

    def clear_expired(self):
        for code, lesson in list(self.lessons.items()):
            if not lesson.is_active():
                del self.lessons[code]
                for key in [k for k in self.rooms if k[0] == code]:
                    del self.rooms[key]
                if self.db:
                    self.db.delete_lesson(code)

    def get_lesson(self, code):
        self.clear_expired()

        if code in self.lessons:
            return self.lessons[code]

        if self.db:
            data = self.db.get_lesson_from_db(code)
            if data:
                lesson = Lesson(
                    lesson_name=data["lesson_name"],
                    lesson_code=data["lesson_code"],
                    duration_minutes=data["duration_minutes"],
                    end_time=data["end_time"],
                    appendices=data["appendices"]
                )
                self.lessons[code] = lesson
                return lesson

        return None

    def open_lesson(self, teacher_name, password, code, lesson_name, duration):
        if self.db:
            self.db.save_lesson(code, lesson_name, teacher_name, duration)

        lesson = Lesson(lesson_name, code, duration)
        self.lessons[code] = lesson
        self.teachers[code] = Teacher(teacher_name, password, code)
        return self.teachers[code], lesson

    def get_teacher(self, name, password, code):
        teacher = self.teachers.get(code)
        if not teacher:
            teacher = Teacher(name, password, code)
            self.teachers[code] = teacher
        return teacher

    def add_link(self, teacher, lesson, link):
        teacher.add_link(lesson, link)
        if self.db:
            self.db.add_appendix_to_db(lesson.lesson_code, link)

    def join(self, name, lesson):
        student = self.find_student(lesson, name)
        if student:
            return student

        student = Student(name, lesson.lesson_code)
        student.join_lesson(lesson)
        return student

    def find_student(self, lesson, name):
        for student in lesson.students:
            if student.name == name:
                return student
        return None

    def accept_help(self, teacher, lesson, student):
        url = create_room_url()
        self.rooms[(lesson.lesson_code, student.name)] = url
        teacher.resolve_help(student)
        return url

    def get_room(self, lesson, name):
        return self.rooms.get((lesson.lesson_code, name))

    def close_room(self, lesson, name):
        self.rooms.pop((lesson.lesson_code, name), None)
