# map function

numbers =[1,2,3,4,5]

# creates the list of nsquare of each elemnt list

def square(a):
    return a*a

squares= list( map(square,numbers))

print(squares)

# we can also lamda function

squares2=list( 
    map( lambda a: a*a , numbers)
)

print(squares2)

# by list comprehasion

squares3= [el*el for el in numbers]
print(squares3)