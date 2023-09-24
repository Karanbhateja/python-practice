# We can use normal parameters with *args, it will take first input as separate and then all others in a tuple
# And also we cannot write normal parameter after *args because then all the arguments will go in args.
def multiply(num, *args):  # We can leave *args empty because it is a tuple but we cannot leave num empty
  print(num)
  print(args)
  result=1
  for i in args:
    result*=i
  return result

print(multiply(3,4,5,6))

## OUTPUT- 
# 3
# (4,5,6)
# 120
