# *args is usually passsed in parameter to the function and it is used when we do not know how many arguments are going to be there in the function

def total(*args): # Now This function will take a tuple as a arguments/ will store all the inputs in a tuple. And here the name of that tuple will be 'args'
  print(args)     # We can write anything instead of args but according to the convention we write args


def summ(*args):
  total = 0
  for num in args:
    total += num
  return total

print(summ(1,7,3,9)) # Different arguments
print(summ(1,7,3,9,7,2,8,5)) # Different arguments
