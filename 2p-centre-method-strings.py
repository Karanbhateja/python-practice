# center method is used to add same sign or word on both sides if the string.
name = "Mr Robot"
print(name.center(10,"*"))
# variable.center(lenght+no. of characters to add on both sides , "character to add")

name = input("Enter your name : ")
print(name.center(len(name) + 4, "*"))
# This will add 2 stars on both sides of the name