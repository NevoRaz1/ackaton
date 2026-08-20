

class Lesson:
    def __init__(self,teacher, lesson_name: str, lesson_code: int, lesson_duration: int=45, lesson_appendices=None,students_list=None,):
        if lesson_appendices is None:
            self.lesson_appendices=[]
        else:
            self.lesson_appendices=lesson_appendices
        if students_list is None:
            self.students_list=[]
        else:
            self.students_list=students_list
        self.lesson_name = lesson_name
        self.lesson_code = lesson_code
        if int(lesson_duration)<0:
            self.lesson_duration=0
        else:
            self.lesson_duration=lesson_duration
        self.teacher=teacher



    def add_appendix(self, appendix_link: str):
        self.lesson_appendices.append(appendix_link)

    def add_student(self, student):
        self.students_list.append(student)