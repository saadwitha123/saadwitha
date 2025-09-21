#Passing Members of One Class to Another Class
class A:
    def __init__(self, value):
        self.value = value
class B:
    def __init__(self, obj):
        self.obj = obj
a = A(10)
b = B(a)
print(b.obj.value)




class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")
class School:
    def __init__(self, student_obj):
        self.student = student_obj
    def show_student_info(self):
        print("Student Information from School class:")
        self.student.display()
s1 = Student("Rahul", 101)
school_obj = School(s1)
school_obj.show_student_info()
