# Differences between Methods and Constructors
class Test:
    def __init__(self):
        print("Constructor")
    def show(self):
        print("Method")


t = Test()
t.show()



# Difference Between Constructor and Method in Python
# Constructor (__init__)
# Special method that automatically runs when an object is created.
# Used for initializing instance variables.
# Defined using def __init__(self, ...):
# Method
# Normal function defined inside a class.
# Used to define behavior (operations) of an object.
# Called explicitly using object.method_name().
class Student:
    # Constructor: runs automatically when object is created
    def __init__(self, name, marks):
        self.name = name        # Instance variable
        self.marks = marks
        print("Constructor called: Object initialized")

    # Method: user has to call explicitly
    def display_info(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

    # Another Method
    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Marks updated for {self.name}")


# Creating object → constructor runs automatically
s1 = Student("Rahul", 85)

# Calling methods explicitly
s1.display_info()
s1.update_marks(90)
s1.display_info()
