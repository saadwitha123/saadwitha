import inspect

# Global variables
x = 10
y = "hello"

# Functions
def greet():
    return "Hi"

def add(a, b):
    return a + b

# Classes
class A:
    def method_a(self):
        return "Class A"

class B:
    def method_b(self):
        return "Class B"

current_module = __import__(__name__)   # import current file as module

# Get all classes
classes = inspect.getmembers(current_module, inspect.isclass)

# Get all functions
functions = inspect.getmembers(current_module, inspect.isfunction)

# Get all global variables (exclude builtins, functions, classes)
global_vars = [
    name for name, value in inspect.getmembers(current_module)
    if not (inspect.isfunction(value) or inspect.isclass(value) or name.startswith("__"))
]

# Print details
print("Classes:", [c[0] for c in classes])
print("Functions:", [f[0] for f in functions])
print("Global Variables:", global_vars)

print("\nCounts:")
print("Number of Classes:", len(classes))
print("Number of Functions:", len(functions))
print("Number of Global Variables:", len(global_vars))
