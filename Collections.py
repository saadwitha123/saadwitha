import collections
print(dir(collections))  # Shows all collection classes




import collections
# 1. Counter - counts occurrences of elements
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_counter = collections.Counter(fruits)
print("Counter Example:", fruit_counter)

# 2. namedtuple - like a lightweight class with named fields
Point = collections.namedtuple("Point", ["x", "y"])
p1 = Point(10, 20)
print("namedtuple Example:", p1.x, p1.y)

# 3. deque - fast queue that supports append & pop from both ends
dq = collections.deque([1, 2, 3])
dq.appendleft(0)  # add to left
dq.append(4)      # add to right
print("Deque Example:", dq)

# 4. defaultdict - dictionary with default values
dd = collections.defaultdict(int)  # int() default is 0
dd["a"] += 1
dd["b"] += 2
print("defaultdict Example:", dd)

# 5. OrderedDict (Python 3.7+ normal dicts also remember order)
od = collections.OrderedDict()
od["first"] = 1
od["second"] = 2
print("OrderedDict Example:", od)

# Counter
# Counts how many times each element occurs.
# Example: {'apple': 3, 'banana': 2, 'orange': 1}
# namedtuple
# Creates simple classes for grouping data.
# Example: Instead of using a tuple (10,20), you can use Point(x=10, y=20).
# deque (Double-Ended Queue)
# Faster than lists for adding/removing items at both ends.
# Example: [0,1,2,3,4].
# defaultdict
# Automatically creates a default value if a key doesn’t exist.
# Example: if you access dd['c'], it will return 0 instead of an error.
# OrderedDict
# Like a normal dict, but remembers the order keys were inserted (before Python 3.7, dicts didn’t guarantee order).