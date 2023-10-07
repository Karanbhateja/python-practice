# The map() function in Python is a built-in function used to apply a given function to all items in an iterable (e.g., list, tuple) and return a map object, which can be converted to a list or other iterable types.

# Let's start with a simple example:

# Define a function to square a number
def square(x):
    return x ** 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Using the map() function to square each number in the list
squared_numbers = map(square, numbers)

# The result is a map object. To see the squared numbers, convert it to a list
squared_numbers_list = list(squared_numbers)

# Printing the squared numbers
print(squared_numbers_list)

# The map() function takes two arguments: the first argument is the function you want to apply to each item, and the second argument is the iterable you want to process.

# You can also use lambda functions with map() for simple operations:

# Using lambda function to cube each number in the list
cubed_numbers = map(lambda x: x ** 3, numbers)

# Converting the result to a list
cubed_numbers_list = list(cubed_numbers)

# Printing the cubed numbers
print(cubed_numbers_list)

# The map() function is commonly used to transform data in iterables without using explicit loops. It's a powerful tool for data manipulation and processing.

# Note: In Python 3, map() returns a map object, so you often convert it to a list or another iterable type to see the results.
