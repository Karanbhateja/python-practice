# The zip() function in Python is used to combine multiple iterables, such as lists, tuples, or strings, element-wise into tuples. It creates an iterator that generates these tuples.

# Syntax:
# zip(iterable1, iterable2, ...)

# Example 1 - Basic Usage:
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
last_names = ["Wick", "Smith", "Putt"]
# Using zip() to combine names and scores
# Converting the zip object to a list (optional):
combined_list = list(zip(names, scores, last_names)) # or we can make dictionary too by using dict but it can be only done if there are 2 lists only

print(combined_list)
# Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Example 2 - Unequal Length Iterables:
fruits = ["Apple", "Banana", "Cherry"]
colors = ["Red", "Yellow"]

# Using zip() to combine fruits and colors, this will give a iterator
# Converting the zip object to a list (optional):
combined_dict = dict(zip(fruits, colors))

print(combined_dict)
# Output: [('Apple', 'Red'), ('Banana', 'Yellow')]

# The zip() function combines elements until the shortest iterable is exhausted. In this example, "Cherry" from the fruits list is not included.

# Example 3 - Unpacking with zip():
# You can also use zip() to unzip (extract) data from tuples.

zipped_data = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Unpacking names and scores from zipped_data:
unzipped_names, unzipped_scores = zip(*zipped_data)

print(unzipped_names)
# Output: ('Alice', 'Bob', 'Charlie')

print(unzipped_scores)
# Output: (85, 92, 78)

# Summary:
# - The zip() function combines iterables element-wise into tuples.
# - It stops when the shortest iterable is exhausted.
# - You can use zip() for data alignment or pairing items from multiple lists.
# - To unzip data, use the * operator with zip().

# The zip() function is a powerful tool for various data manipulation tasks, such as merging data from different sources or creating dictionaries from parallel lists.
