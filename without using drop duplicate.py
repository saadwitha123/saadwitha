#without using drop duplicate write a python code

data = [1, 2, 2, 3, 4, 4, 5]

unique_list = []
for item in data:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
