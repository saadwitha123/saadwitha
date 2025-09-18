# Self Variable
class Student:
    i=90
    def show(self):
        print("self refers to:", self)
     

s = Student()
s.show()
s.j = 100
s.show()

s2 = Student()
s2.show()
s2.j = 200
s2.show()   


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):  #using self to access instance variable
        print("name:", self.name)
        print("age:", self.age)
s1 = student("saadwitha", 20)
s2 = student("ramya", 22)
s3 = student("neha", 32)
s1.show()
s2.show()
s3.show()