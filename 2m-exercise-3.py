name , singchar = input("Enter your name and a single character : ").split()

print(f"Lenght of your name is {len(name)} ")
print(f"Character count is : {name.lower().count(singchar)}")