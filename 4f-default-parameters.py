def user_info(firstname,lastname = None,age = None):
    print(f"Your first name is {firstname}")
    print(f"Your last name is {lastname}")
    print(f"Your age is {age}")

user_info("Mr",)
# Now if we don't pass one of these values here while callling the function then it will give error.

# But of i define the function with-
#       def user_info(firstname,lastname,age = 23)
#   Now the if we don't input any age then the age will be 23 by default that's why these are called as default parameters.
#   If we input anything then that input will takeover the default parameter.

# But we connot do this - 
#       def user_info(firstname,lastname = 'None' ,age)
# We can only make default parameter in last.