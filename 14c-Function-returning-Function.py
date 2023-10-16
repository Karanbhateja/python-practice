def outer_func():  # First Function
  def inner_func():  # Defining function inside the function (Second Function)
    print("This is the inner function")
  return inner_func   # Here we have returned inner_func , without execcuting not inner_func() with execution

var = outer_func()  # In outer func we did not executed the inner func so the var will have inner_func not inner_func() 
                    # inner_func will not be executed untill we donot use var()

print(var) # Output - <function outer_func.<locals>.inner_func at 0x7fba5bd06d40>
var() # Output - This is the inner function

# ------------------------------------------- PRACTICE -----------------------------------------------------------------

def to_power(x):
  def calculcate_power(n):
    return n**x
  return calculate_power          # Will return the calculate_power without execution

square = to_power(2)
square(5)            # Executing calculate_power

cube = to_power(3)
cube(5)             # Executing calculate_power
