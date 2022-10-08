def last_char(n):
    return n[-1]
name = input("Enter your name: ")
print(last_char(name))


def odd_even(num):
    if num%2 == 0:
        return"even"
    else:
        return "odd"
# This is the normal way

def odd_even(num):
    if num%2 == 0:
        return"even"
    return "odd"

# This and the function aboove this means same here, function will return even only when the quotiwnt is zero else it will skip the if code and pront odd but in opposite case it will return even and will exit and that's the same thing as the above code.

# Now with Boolean values-

def is_even(num):
    if num%2==0:
        return True
    return False

# Here True and False are Boolean values.

# We can make it even more shorter here's how -

def is_even_short(numb):
    return numb%2==0
# Now this function will automatically return boolean values because we have'nt used any if else code or written what to return for which condition.
print(is_even_short(5))

#  HERE NUMB IS PARAMETER (WHICH WE'VE USED IN FUNCTION) AND 5 IS ARGUMENT (WHICH WE'VE GIVEN WHEN WE CALLED THE FUNCTION)