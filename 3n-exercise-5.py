name = input("Enter your name: ")
tempvalue=""
i = 0
while i< len(name):
    if name[i] not in tempvalue:
        print(f"{name[i]} is present {name.lower().count(name[i])} times in {name}")
        tempvalue+= name[i]
    i+=1