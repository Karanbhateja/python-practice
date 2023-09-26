# Lambda Expression (Anonymous Function)
# When we define a funtion it gets stored in memory and we can check it by print(function_name) but lambda function doesnot gets stored like function in the memory like that

# We can define lamba function by using lambda  keyword -
lambda a,b : a+b
  # Inputs  Functionality

# To use it we can store it in a variable -
add = lambda a,b : a+b
# We usually do not store lambda function in a variable but here for example only we have done it, lambda functions are used with map, filter, reduce functions in python.
print(add(2,3))
