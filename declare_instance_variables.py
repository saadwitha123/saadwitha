# Where we can declare Instance Variables
#inside constructor
#inside instance method 
#outside the class using object reference variable

class Student:
    def __init__(self, name):
        self.name = name
    # instance method example of declaring instance variable
    def set_age(self, age):
        self.age = age

obj = Student("John")
obj.set_age(20)
#declaring instance variable outside the class using object reference variable
obj.age=20  
print(obj.name)  # Output: John
print(obj.age)   # Output: 20   


obj2 = Student("Ajay")
obj2.set_age(24)

print(obj2.name)  # Output: John
print(obj2.age)   # Output: 24  


obj3 = Student("Sashi")
obj3.set_age(20)


print(obj3.name)  # Output: John
print(obj3.age)   # Output: 20


print(obj.__dict__)  # Output: {'name': 'John'}
print(obj2.__dict__)  # Output: {'name': 'Ajay', 'age': 30}
print(obj3.__dict__)  # Output: {'name': 'Sashi', 'age': 40}

del obj.age  # Deleting instance variable age from obj
del obj2.age  # Deleting instance variable age from obj2
del obj3.age  # Deleting instance variable age from obj3

print(obj.__dict__)  # Output: {'name': 'John'}
print(obj2.__dict__)  # Output: {'name': 'Ajay', 'age': 30}
print(obj3.__dict__)  # Output: {'name': 'Sashi', 'age': 40}


# What is an Instance Variable?
# An instance variable is a variable that is defined inside a class, but associated with objects (instances) of that class.
# Each object gets its own copy of instance variables.
# They are usually defined inside the __init__() constructor using self.
class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def display (self):
        print(f"Iam {self.name} and my rollno is {self.rollno}")
s1 = student("sneha", 10)
s2 = student("priya", 14)
s1.display()
s2.display()