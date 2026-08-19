from Lesson import Lesson


class Student:
    def __init__(self, name: str, lesson_code: int):
        self.name = name
        self.lesson_code = lesson_code
        self.need_help = False
        self.current_lesson = None

    def join_lesson(self, lesson: Lesson) -> bool:
        if self.lesson_code == lesson.lesson_code:
            self.current_lesson = lesson
            lesson.add_student(self)
            return True
        return False

    def get_links(self):
        if self.current_lesson:
            return self.current_lesson.lesson_appendices
        return []

    def request_help(self):
        self.need_help = True

    def cancel_help_request(self):
        self.need_help = False