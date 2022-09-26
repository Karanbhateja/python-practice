# variable.replace("what to replace" , "what to be replaced with" , how many times ) method can be used.
line = "He is a good driver is "
print(line.replace("is", "was",1))

# Find method is used to find any character or word in a string or variable.
# variable.find("what to fing" , from which position to start search form)

print(line.find("is", 5))

# to find the position of second is wthout knowing the position of 1st is.

is_pos1 = line.find("is")
print(line.find("is", is_pos1+1))
# we added +1 because it will start searching from there only and will find is on that position immidieately which is first is.