#write a python code use Between without pandas

def is_between(value, lower, upper):
    return lower <= value <= upper

num = 25
print(is_between(num, 10, 30))   
print(is_between(num, 30, 40))   
