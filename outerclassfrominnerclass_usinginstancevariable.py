class Outer:
    def __init__(self, name, age):
        self.name = name        # instance variable
        self.age = age          # instance variable

    class Inner:
        def __init__(self, outer_instance):
            # store reference of outer object
            self.outer = outer_instance

        def display(self):
            # access outer instance variables
            print(f"Name: {self.outer.name}, Age: {self.outer.age}")

# Create outer object
outer_obj = Outer("Saad", 21)

# Create inner object and pass outer_obj
inner_obj = Outer.Inner(outer_obj)

# Access outer's instance variables from inner
inner_obj.display()
