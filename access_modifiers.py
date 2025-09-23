#code example for Public, Private and Protected Members

class Demo:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
    def show(self):
        print(self.public, self._protected, self.__private)
d = Demo()
d.show()
print(d.public)
print(d._protected)
# print(d.__private) # Error
print(d._Demo__private) # Access private
# Name mangling to access private member
# Private members are not accessible directly outside the class but can be accessed using name mangling.
# Protected members are accessible within the class and its subclasses but should be treated as non-public.
# Public members are accessible from anywhere.  
# In Python, these are just conventions and do not enforce access restrictions like in some other languages.
#mangling code example
class Test:
    def __init__(self):
        self.__private_var = 42  # Private variable

    def get_private_var(self):
        return self.__private_var  # Public method to access private variable   
t = Test()
# print(t.__private_var)  # This will raise an AttributeError   
print(t.get_private_var())  # This will work and print 42
print(t._Test__private_var)  # Accessing the private variable using name mangling   
# Name mangling is a mechanism in Python that alters the name of private variables to prevent accidental access and modification from outside the class.
# It is done by prefixing the variable name with _ClassName.

#TODO mangling
# Public → no underscore (variable)
# Protected → single underscore (_variable)
# Private → double underscore (__variable)
class Student:
    def __init__(self, name, age, grade):
        self.name = name            # Public
        self._age = age             # Protected
        self.__grade = grade        # Private

    # Public method
    def show(self):
        print("Name:", self.name)
        print("Age:", self._age)            # Accessible
        print("Grade:", self.__grade)       # Accessible inside class

    # Getter for private variable
    def get_grade(self):
        return self.__grade

s = Student("Alice", 20, "A")
print(s.name)        
print(s._age)        
print(s.get_grade()) 
print(s._Student__grade)  