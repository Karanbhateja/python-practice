def greatest(a,b,c):
    if a>b and a>c:
        return f"{a} is greatest"
    elif b>a and b>c:
        return f"{b} is greatest"
    elif c>a and c>b:
        return f"{c} is greatest"
    else:
        return "All the numbers are equal"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

print(greatest(num1, num2, num3))