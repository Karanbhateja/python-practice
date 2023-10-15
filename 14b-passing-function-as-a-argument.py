# In map function we pass a function as an argument like - map(square, l)
# We can also make a custom function like map which takes a function as a argument

def square(x): # Function to be passed
  return x*x
  
l = [1,2,3,4,5]

def my_map(func, l):
  # here func is any function and l is any iterable 
  new_list=[]
  for item in l:
    new_list.append(func(item))
  return new_list

print(my_map(square, l))

# We can also use lambda function
print(my_map(lambda x : x*x, l))
