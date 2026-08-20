from Lesson import Lesson
from Student import Student
def student_interaction(student:Student):
    while True:
        number=int(input("type 1 if you want to request for help \n type 2 if you want to cancel the help request\nenter here: "))
        while number != 1 and number != 2:
            number=int(input("invalid number. \ntype 1 if you want to request for help \n type 2 if you want to cancel the help request\nenter here:"))
        if number==1:
            student.request_help()
        else:
            student.cancel_help_request()