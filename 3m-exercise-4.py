number = input("Enter the number : ")
lenght = len(number)
sum = 0
i = 0
while i < lenght:
    sum = sum + int(number[i])
    i += 1

print(sum)

#              OR
# i = 1
# while i <= lenght:
#     sum = sum + int(number[i-1])
#     i += 1

# print(sum)