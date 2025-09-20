# Various Places to declare Static Variables
class Student:
    school = "ABC School"  # Inside class
    def __init__(self):
        Student.school = "XYZ School"  # Inside constructor
    def set_school(self):
        Student.school = "New School"  # Inside method




class Student:
    # Static variable (shared by all objects)
    school_name = "ABC High School"

    def __init__(self, name, roll_no):
        # Instance variables (unique for each object)
        self.name = name
        self.roll_no = roll_no

    def display(self):
        # Accessing instance and static variables
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School: {Student.school_name}")


# Creating objects
s1 = Student("Alice", 1)
s2 = Student("Bob", 2)

# Display details
s1.display()
s2.display()

# Changing static variable using class name
Student.school_name = "XYZ Public School"

print("\nAfter changing static variable:")

s1.display()
s2.display()
