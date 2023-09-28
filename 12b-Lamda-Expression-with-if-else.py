# LAMBDA EXPRESSION WITH IF ELSE

# Taking this function for example-
def fun(s):
  if len(s)>5:
    return True
  else:
    return False
# OR we can do - 
def fun_short(s):
  return len(s)>5

# Now lets define this with Lambda expression
fun_lambda = lambda s: True if len(s) > 5 else False
# OR we can also do -
fun_lambda_short = lambda s: len(s) > 5

# --------------------- Practice --------------------------------

# Let's define a normal function first and then we will define it's equivalent with lambda Expression
def is_even(a):
  if a%2==0:
    return True
  return False
print(is_even(3))

# This Function can also be defined as - 
def is_even(a):
  return a%2 == 0

# Now by Lambda Expression -
is_even2 = lambda a: a%2==0
print(is_even2(6))
