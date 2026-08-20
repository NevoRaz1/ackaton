# 1 is for creating lesson
# 2 is for student or teacher to join to the class
from Lesson import Lesson
from Teacher import Teacher
def create_teacher(teacher_name,teacher_password,lesson_code):
    teacher=Teacher(teacher_name,teacher_password,lesson_code)
    return teacher
def create_lesson(teacher,lesson_name,lesson_code,lesson_duration,lesson_appendices,students_list):
    lesson=Lesson(teacher,lesson_name,lesson_code,lesson_duration,lesson_appendices,students_list)
    return lesson
def what_to_do(what_to_do: int):
    if what_to_do == 1:
        print("welcome to Smart Class IL\nyou are now loggin as a teacher")
        teacher_name=input("enter your name: ")
        teacher_password=input("enter your password: ")
        lesson_code=int(input("enter the lesson password"))
        teacher=create_teacher(teacher_name,teacher_password,lesson_code)


        print(f"welcome {teacher_name} \n now we are about to create the lesson please fill the following questions")
        lesson_name=input("enter lesson name: ")
        lesson_code=input("enter lesson code: ")
        lesson_duration=input("enter lesson duration: ")
        lesson_appendices=[]
        appendix=" "
        while appendix!="done":
            appendix=input("enter the appendix (to stop adding appendices type done ):  ")
            if appendix!="done":
                lesson_appendices.append(appendix)
        students_list=[]
        create_lesson(teacher,lesson_name,lesson_code,lesson_duration,lesson_appendices,students_list)

what_to_do(1)
