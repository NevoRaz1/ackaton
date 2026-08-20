# 1 is for creating lesson
# 2 is for student or teacher to join to the class
from Lesson import Lesson
from Teacher import Teacher
from Student import Student
def create_student(student_name,lesson_code):
    student=Student(student_name,lesson_code)
    return student
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


        print(f"welcome {teacher_name} \nnow we are about to create the lesson please fill the following questions")
        lesson_name=input("enter lesson name: ")
        lesson_code=input("enter lesson code: ")
        lesson_duration=input("enter lesson duration in minutes: ")
        appendix = input("enter the appendixes, make space between each link for it to enter it properly:  ")
        lesson_appendices = appendix.split(" ")
        students_list=[]
        teacher=create_teacher(teacher_name,teacher_password,lesson_code)
        create_lesson(teacher,lesson_name,lesson_code,lesson_duration,lesson_appendices,students_list)
    elif what_to_do==2:
        print("welcome to Smart Class IL\nyou are now about to loggin as a student")
        student_name=input("enter your name: ")
        lesson_code=input("enter the lesson code of the class you want to join: ")
        while lesson_code!=lesson.lesson_code:
            lesson_code=input("invalid class code please try again: ")

        student=create_student(student_name,lesson_code)
        lesson.add_student(student)
        print("you are now in the class!")

