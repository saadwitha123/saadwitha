# How to Delete Static Variables of a Class
class Student:
    school = "ABC School"
    def __init__(self, school):
        self.school = school
del Student.school





class Student:
    # Static variable
    school_name = "ABC High School"

    def __init__(self, name):
        self.name = name

    def display(self):
        # Using getattr() to avoid error if static variable is deleted
        school = getattr(Student, "school_name", "Not Available")
        print(f"Name: {self.name}, School: {school}")


# Create objects
s1 = Student("Alice")
s2 = Student("Bob")

s1.display()
s2.display()

# Delete static variable
del Student.school_name

print("\nAfter deleting static variable:")

s1.display()
s2.display()