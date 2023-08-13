#  Anything can be stored in a list - Words, numbers, Float......
#  A list is initialised by Square Bracktes []

words = ["one", "two", "Three"]
print(words)

numbers = [1,2,3]
print(numbers)

# A single List can store mixed values, or different type of data 

mixed = [1, "two", 2.3, "Two point four"]
print(mixed)

# ACCESSING THE LIST ELEMENTS (Same as Strings)

print(mixed[1]) # Will print the second item of the list Mixed
print(mixed[-1]) # Will print the element from the last
print(mixed[:3]) # Will print till the 2 item of the List

# UPDATING LIST ELEMENTS (Same as Strings)

mixed[0] = 2 # Will update the first element of the list to 2
print(mixed)
