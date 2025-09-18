class Outer:
    # static variable (class variable)
    static_var = "I am static variable of Outer class"

    class Inner:
        def display(self):
            # Access using Outer class name
            print("Accessing from Inner class:", Outer.static_var)
# Usage
outer_obj = Outer()
inner_obj = outer_obj.Inner()
inner_obj.display()
