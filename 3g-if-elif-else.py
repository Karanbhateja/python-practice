age = int(input("Enter your age : "))

if age<=0:
    print("Wrong Input")
elif 0<age<=10: # elif is used there are multiple code blocks for a condition.
    print("Ticket Price : 100")
elif 10<age<=18:
    print("Ticket Price : 150")
elif 18<age<=60:
    print("Ticket Price : 200")
else:
    print("Ticket Price : 180")