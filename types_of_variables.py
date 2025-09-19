# Types of Variables
# Instance, Static, and Local variables

#self variable is default instance variable available in the class
#Instance variable is the variable which is declared inside the constructor using self keyword  
#Static variable is the variable which is declared inside the class but outside the constructor
#Local variable is the variable which is declared inside the method


class Demo:
    # Static variable (class variable)
    """example class for types of variables"""
    static_var = "I am static!"

    def __init__(self, value):
        # Instance variable
        self.instance_var = value

    def show(self):
        # Local variable
        local_var = "I am local!"
        print("Instance variable:", self.instance_var)
        print("Static variable:", Demo.static_var)
        print("Local variable:", local_var)

d = Demo("I am instance!")
d.show()



# Instance Variables – Belong to objects (different objects can have different values).
# Class Variables (Static Variables) – Shared across all objects of a class.
# Local Variables – Declared inside a method/function and exist only within it.
class Student:
    # Class Variable (shared by all objects)
    school_name = "ABC High School"

    def __init__(self, name, age):
        # Instance Variables (unique to each object)
        self.name = name
        self.age = age

    def display_info(self):
        # Local Variable (exists only inside this method)
        grade = "10th Grade"
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.school_name}, Grade: {grade}")


# Creating objects
s1 = Student("Rahul", 15)
s2 = Student("Priya", 14)

# Accessing instance and class variables
s1.display_info()
s2.display_info()

# Changing instance variable (only for s1)
s1.age = 16

# Changing class variable (affects all objects)
Student.school_name = "XYZ International School"

print("\nAfter modifications:")
s1.display_info()
s2.display_info()
