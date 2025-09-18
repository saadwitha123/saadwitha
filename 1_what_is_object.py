# What is Object?
# An object is an instance of a class.

class Person:
    pass

obj1 = Person()

class Student:
    pass
nikshan = Student()

class Automobile:
    tires="tires"   #//2 bytes
    def func(self):   #// 7 Bytes
        a=90  #// 1byte
        print("")

BMW = Automobile()  # 10 bytes
print(BMW.tires)
BMW.func()
Thar = Automobile()  #bytes
Hummer = Automobile()
Audi = Automobile()



class car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    def output(self):
        print(f"This car is {self.color} {self.brand}")
car1 = car("pink", "BMW")
car2 = car("white", "thar")
print(car1.color)
print(car1.brand)
car2.output()