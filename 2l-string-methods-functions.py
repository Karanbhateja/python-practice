name = "Mr Robot"

# len() function
# len function counts the no. of letters in a string it also counts the spaces.

print(len(name))

# lower() Method
# Lower method converts every letter of a string to lower case.

print(name.lower())

# upper() Method
# Upper method converts every letter of a string to upper case.

print(name.upper())

# title() Method
# Title Method converts first letter after space to upper case.

print(name.title())

# count() Method
# Count method counts a particular character in a string, you can write the character inside ("") that you wnat count, it is case sensitive.

print(name.count("o")) 

# isUpper() and isLower() Function
#  When a character is passed in isUpper() Function then it tells that is a character is in Upper case or not by returning True or False
# When a character is passed in isLower() Function then it tells that is a character is in lower case or not by returning True or False
print(name[0],isUpper())  # This will return True, as M is in Upper case in Mr Robot
print(name[1],isLower())  # This will return True, as r is in Lower case in Mr Robot
