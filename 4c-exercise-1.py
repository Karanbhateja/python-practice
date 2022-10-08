def greates_in_two(a,b):
    if a>b:
        return f"{a} is greater"
    elif a<b:
        return f"{b} is greater"
    else:
        return "both the numbers are equal"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(greates_in_two(num1, num2))
