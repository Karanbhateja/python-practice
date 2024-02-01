# kwargs -> keyword arguments 
# **kwargs (double star operator)

#kwargs as parameter
# ** double star opeartor take key value pari as argument and convert it into the 
# dictionary 
## it is like dict(key1=value1,key2=value2) function which converts the parameter into the dictionary
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key in kwargs:
        print(f"{key}:{kwargs[key]}")

func(first_name="Kailash",middle_name="Kumar",last_name="Mandal")

# dictionary unpacking 
dic={
    "name":"Kailash",
    "age":22
}

#use ** operator to split the dictionary key value pairs
func( **dic)

## all types parameters

# parameters
# *args
# default parameters
# **kwargs

def funct(name , *args,last_name="unknown",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

funct("Karan",1,2,3,last_name="Mandal",a=1,b=2 )