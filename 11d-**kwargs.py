# **kwargs are also similar to *args, as *args took input as tupple, on the other hand **kwargs take input as a dictionary
def display(**kwargs):
    print(kwargs)
# Iteration
    for k,v in kwargs.items():
        print(f"{k} : {v}")

display(first_name="John" ,last_name="Wick") # Now this information will be stored in a dictionary with first_name & last_name as key and "John" & "Wick" as values

# WITH NORMAL PARAMETER
# With normal parameter **kwargs works same as *args

def norm_param(name, **kwargs):
  print(name)
  print(kwargs)

norm_param("John Wick", first_name="Tony" ,last_name="Stark")
# OUTPUT - 
# John Wick
# {'first_name': 'Tony', 'last_name': 'Stark'}

# DICTIONARY UNPACKING
# Like we did in args, in same manner we can do with kwargs 
d= {first_name="John" ,last_name="Wick"}
display(**d)
