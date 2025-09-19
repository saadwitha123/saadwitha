# What are Variable Arguments?
# In Python, sometimes we don’t know how many arguments a function will receive.
# We can handle this using:
# *args → for variable positional arguments (tuple)
# **kwargs → for variable keyword arguments (dictionary)

#Using *args
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(10, 20))
print(add_numbers(1, 2, 3, 4, 5))

#Using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_details(name="Saad", age=22, city="Hyderabad")
