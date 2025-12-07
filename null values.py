#Print NULL (None) values from a list

data = [10, None, 25, None, 40, 50]

for value in data:
    if value is None:
        print("NULL value found")



#Find the positions (indexes) of NULL values

data = [10, None, 25, None, 40, 50]

null_positions = []

for i in range(len(data)):
    if data[i] is None:
        null_positions.append(i)

print("Positions of NULL values:", null_positions)


#Remove NULL values

data = [10, None, 25, None, 40, 50]

cleaned_list = [x for x in data if x is not None]

print(cleaned_list)
