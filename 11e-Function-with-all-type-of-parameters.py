# Suppose we have to meke a function with all type of parameters (Normal parameter, Default parameter, *args, **kwargs)
# Then the order in the parameter that we have to follow always should be PADK (Parameter, Args, Default, Kwargs)
# If this order is not followed then error will occur

def func(name, *args, age=24, **kwargs): # We cannot change this order either we use all type of paramters or some of them
  print(name)
  print(args)
  print(age)
  print(kwargs)

func("John", 1,2,3,4, a=1,b=2,c=3) 
# # OUTPUT
# John
# (1, 2, 3, 4)
# 24
# {'a': 1, 'b': 2, 'c': 3}
