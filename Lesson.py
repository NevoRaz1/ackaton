from datetime import datetime, timedelta


class Lesson:
    def __init__(self, lesson_name: str, lesson_code: int, duration_minutes: int, end_time: datetime = None, appendices=None):
        self.lesson_name = lesson_name
        self.lesson_code = lesson_code
        self.duration_minutes = duration_minutes
        self.end_time = end_time if end_time else datetime.now() + timedelta(minutes=duration_minutes)
        self.lesson_appendices = appendices if appendices is not None else []
        self.students = []

    def get_remaining_time(self) -> int:
        remaining = (self.end_time - datetime.now()).total_seconds()
        return max(0, int(remaining))

    def is_active(self) -> bool:
        return self.get_remaining_time() > 0

    def get_formatted_time(self) -> str:
        seconds = self.get_remaining_time()
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"

    def add_appendix(self, appendix_link: str):
        self.lesson_appendices.append(appendix_link)

    def add_student(self, student):
        self.students.append(student)