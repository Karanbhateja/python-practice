# Suppose we have to pass list as a argument when the function has *args as a parameter then, 
def add(*args):
  for i in args:
    result += i
  return result

# List -
l = [1,2,3,4] # Now we want to use this list as argument to the multiply function

print(multiply(*l))

# We can use * to unpack the list/ another tupple and pass its elements to the function
