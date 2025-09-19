#code for hierarchical inheritance concept
# class B(A): pass
# class C(B): pass
# print(C.mro())

# class D(A): pass
# class E(A): pass
# class F(B): pass



# Parent class
class A:
    def display(self):
        print("I am from class A (Parent)")

# Child classes (all inherit from A)
class B(A):
    def show_b(self):
        print("I am from class B")

class C(A):
    def show_c(self):
        print("I am from class C")

class D(A):
    def show_d(self):
        print("I am from class D")

class E(A):
    def show_e(self):
        print("I am from class E")

class F(A):
    def show_f(self):
        print("I am from class F")

# Creating objects of child classes
b = B()
c = C()
d = D()
e = E()
f = F()

# Accessing methods
b.display(); b.show_b()
c.display(); c.show_c()
d.display(); d.show_d()
e.display(); e.show_e()
f.display(); f.show_f()
