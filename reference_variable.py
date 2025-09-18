# What is Reference Variable?
class Student:
    name = "name"
    age = 14  




ajay = Student()
vijay= ajay  # s2 is a reference variable pointing to the same object as s1


ajay.age


x = [1, 2, 3]
y = x
print(y)
y.append(4)
print(y)