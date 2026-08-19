from Lesson import Lesson


class Teacher:
    def __init__(self, name: str, password: str, lesson_code: int):
        self.name = name
        self.password = password
        self.lesson_code = lesson_code

    def add_link(self, lesson: Lesson, link: str):
        lesson.add_appendix(link)

    def get_help_queue(self, lesson: Lesson):
        return [student for student in lesson.students if student.need_help]

    def resolve_help(self, student):
        student.cancel_help_request()