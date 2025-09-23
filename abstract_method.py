# Abstract Method
# An abstract method is a method that is declared, but contains no implementation.
# Abstract methods are meant to be overridden in derived classes.   
#same as Java abstract method
# In Python, abstract methods are defined using the abc module, which stands for Abstract Base Classes
#@abstractmethod is mandatory to declare a method as abstract method
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass





from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass 1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Subclass 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Using the classes
shapes = [Rectangle(4, 5), Circle(3)]

for s in shapes:
    print(f"{s.__class__.__name__} Area:", s.area())
