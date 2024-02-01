# lambda expression (anonymous function )

# normal function definition
def add(a,b):
    return a+b


# lambda function definition
add2 = lambda a,b : a+b

print( add2(2,3))

# lambda expression is used in built in function

multiply = lambda a,b : a*b

print( multiply(2,3))

isEven = lambda a : a%2 ==2 

print(isEven(67))

func = lambda s : True if len(s) > 5 else False

print( func("Karan"))

fun = lambda s : len(s)>5

print(fun("karann"))