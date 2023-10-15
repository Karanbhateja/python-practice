# Example 1 - First-Class Functions:
# Functions are first-class citizens, meaning they can be assigned to variables, passed as arguments,
# and returned from other functions.

def square(x):
    return x * x

# Assign a function to a variable.
f = square

# Call the function through the variable.
result = f(5)
print(result)  # Output: 25

print(f)
print(square)
# This will print the address of the location on which the funtion is stored in the memmory boht f and aquare will print the same address 
