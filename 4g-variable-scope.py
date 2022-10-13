x = 5 # Global vairiable ( Outside the function and can be used anywhere in the program )

def func():
    x = 7 # Local Variable ( Inside the functiion and can't be used outisde the function )
    return x

print(func()) # This will print the local variable.

# To work with global variable inside a function we can do - 

def func2():
    global x
    x = 3 # Now here global x is changed to 3 from 5
    return x # This will return the global x because we've written global x in starting of the function.

print(x)
print(func2())