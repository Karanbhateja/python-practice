# filter function

numbers =[1,2,3,4,5,4,6,8,9,10]

#create a list evens[] that contains the even number only

def is_even(a):
    return a%2==0

# creating list using filter( function , list/tuple)
evens =list(
     filter(is_even,numbers)
)

print(evens)

#we can use the lambda expression
print("\nusing lambda expression")
even = list(
    filter(lambda a: a%2==0,numbers )
)

print(even)


print("\nusing list compreshion")
even1= [el for el in numbers if el%2==0]
print(even1)



########################### Iterable and Iterater
# list tuple dictionary stings are iterable
# when a for loop runs it calls iter function that converts the iterable-> iterator

numbers_iter= iter(numbers) # list iterator object type
#then next function next(numbers_iter) is called for 1st item , 2nd item ,3rd item so on...

print(
next(numbers_iter),
next(numbers_iter),
next(numbers_iter),
next(numbers_iter),
next(numbers_iter),
next(numbers_iter)
)

#filter function also return a iterator means next function can be called directly
print(filter(lambda a: a%2==0,numbers ))

print(
next( filter(lambda a: a%2==0,numbers ) )
)
