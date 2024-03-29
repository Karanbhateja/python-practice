# Decorators - Used to increase the functionality of the Function

def func1():
  print("This is function 1")

def func2():
  print("This is function 2")

# Suppose we need to add a new line in func 1 and func 2 without changing the definition of these function
# We can do this by using Decorators

def decorator_function(any_function):
  def wrapper_function():
    print("This is a Awesome Function") # Line to be added 
    any_function()
  return wrapper_function  # Returning the wrapper function without executing it

var = decorator_function(func1) # Now var has the value wrapper_function from the execution of decorator function. So now var = wrapper_function
var()  # Executing Wrapper function 
        # OUTPUT - This is a Awesome Function
        #          This is function 1

# We use @ for decorators
# @ is a syntactic sugar in pytho it makes it easier to read the code and for decorators we use @, here is an example

@decorator_function
def func3():
  print("This is function 3")

# Now instead of storing execution (wrapper function) of decorator function in a variable and then executing that variable, we used @decorator_function just before defining the function
# Now we can directly execute func3 and it will be executed with the decorator 

func3()
