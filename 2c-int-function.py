numb1 = int(input("Enter the first number "))
numb2 = int(input("Enter the second number "))

# int function will convert the input data type to integer instead of string.

sum = numb1 + numb2 
# Now the value stored in sum is integer ecause we added 2 integers.

print("Total is " + str(sum))
# We converted sum to string because we can only add strings with strings not integers with strings.

# str
# 4 --> "4"

# int
# "4" --> 4

# float
# 4 --> 4.0

print("\n Float addition")

n1 = float(input("Enter a number ")) # This will convert the input to float.
n2 = int(input("Enter a number "))

sum2 = n1 + n2
print(sum2)
# If any one input is in float then the result will also become float.