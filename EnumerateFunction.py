# We user enumerate function with for loop to track position of our 
# in iterable

# How we can do this enumerate function
names=['abc','abcdef','xyz']
pos=0
# print 0--> 'abc' ...
for name in names:
    print(f'{pos}--> {name}')
    pos =+1



# with enumerate function
print("\nwith Enumerate function...")
for position,name in enumerate(names):
    print(f'{position}-->{name}')


#task
def findIndex(str_list,str):
    for index,el in enumerate(str_list):
        if el == str:
            return index
    return -1

print( findIndex(
    ['abc','abcdef','xyz'],'xyz'
)) 


