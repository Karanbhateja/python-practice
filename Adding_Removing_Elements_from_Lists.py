# ADDING ELEMENTS TO THE LIST

# Append: Adds an element to the end of the list
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]

# Insert: Adds an element at a specific index
fruits = ["apple", "banana", "orange"]
fruits.insert(1, "grape")
print(fruits)  # Output: ["apple", "grape", "banana", "orange"]

# Extending a List: Adds elements from another list to the end
colors = ["red", "blue"]
colors.extend(["green", "yellow"])
print(colors)  # Output: ["red", "blue", "green", "yellow"]

# REMOVING ELEMENTS FORM THE LIST

# Remove: Removes the first occurrence of a value
animals = ["cat", "dog", "elephant", "dog"]
animals.remove("dog")
print(animals)  # Output: ["cat", "elephant", "dog"]

# Pop: Removes an element at a specific index and returns its value
languages = ["Python", "Java", "C++", "Ruby"]
removed_language = languages.pop(2)
print(removed_language)  # Output: "C++"
print(languages)          # Output: ["Python", "Java", "Ruby"]

# Clear: Removes all elements from the list
numbers.clear()
print(numbers)  # Output: []

# Deleting a List
del colors
# print(colors)   # This line will raise an error since 'colors' no longer exists
