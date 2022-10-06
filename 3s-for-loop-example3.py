name = input("Enter your name : ")
tempvalue = ""

for i in range(len(name)):
    if name[i] not in tempvalue:
        print(f"{name[i]} : {name.lower().count(name[i])}")
        tempvalue+= name[i]
    
