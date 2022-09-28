name = 'abc'
age = 20

if name=='abc' and age==19:
    # Here this code block will only wxecute if both conditions are met if even one of the condition is not met then this code will not be executed.
    # and operator is used when all the conditions need to be true.
    print("Condition True")
else:
    # This code block will be executed even if one condtion is not true.
    print("Condition False")

if name=='abc' or age==19:
    # This code block will be executed when one of any given condition is met.
    print("Condition True")
else:
    # This code block will only be executed when both given condition are false.
    print("Condition False")