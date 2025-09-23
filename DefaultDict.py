from collections import defaultdict

dd = defaultdict(int)  # default value = 0

dd['apple'] += 1
dd['banana'] += 2

print(dd)  # {'apple': 1, 'banana': 2}
print(dd['mango'])  # 0 (no KeyError!)





from collections import defaultdict

# Create a defaultdict with int as default factory
word_count = defaultdict(int)

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Count word frequencies
for word in words:
    word_count[word] += 1

# Print the dictionary
print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# Accessing a missing key
print("grapes ->", word_count["grapes"])  # 0 (default value)








from collections import defaultdict

# defaultdict with int (default value = 0)
dd = defaultdict(int)

# Add values
dd['a'] += 5
dd['b'] += 3

print(dd)        # {'a': 5, 'b': 3}
print(dd['c'])   # 0 (no KeyError!)