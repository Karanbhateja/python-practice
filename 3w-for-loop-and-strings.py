name = "mrrobot"

for i in range(len(name)):
    print(name[i]) # This will print every character of the name string.

# Easy method to do the same is - 

for i in name:
    print(i) # This will also do the same thing.

# This can also be used to add the digits of any number, for ex -

num = input("Enter the number : ")
sum = 0
for i in num:
    sum += int(i)

print(sum)
