# make flexible functions 

# * operator
# *args

def total(a,b):# total function can tak only 2 arguments
    return a+b 

print(
    total(3,4)
)


# * operator converts the all parameters into one tuple(3,4,5,5,6).
def all_total(*args):
    return sum(args)

print(
    all_total(2,3,4,5,5,6)
)

# it can also work like rest operator in js
def all_total1(num,*args):
    print(
        "Value of num is:",num
    )
    return sum(args)+num

print(
    all_total1(2,3,4,5,5,6)
)


# * also work as spread operator like in js
# e.g. :   *[2,3,4,5] -> 2,3,4,5   unpacking of elements of the list


l= [1,2,3,0,4,5]
t= (1,2,3,4,5)
def sum_all(*args):
    return sum(args)

print(
    sum_all(*t) #  here * works as spread operator 
)