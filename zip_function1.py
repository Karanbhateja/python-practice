# zip function
user_id=['user1', 'user2', 'user3']
names=['Karan','Kailash','Rohit']

# use zip function to combine the name and id 
# zip function return the zip object in tuples 

# ('user1', 'Karan'), ('user2', 'Kailash').. which is an iterator
# we can convert iterator(zip object ) into list

print(

    list(
        zip(user_id,names)
    )
)

# w# we can also convert it into dictionary(if only two items tuple are present)
print("\nDictionary format:\n")
print(
    dict(
        zip(user_id,names)
    )
)

last_names=['kumar','singh','rajput']

# zip function also work with three lists
# but with three list dictionary can not be created
print('\nzip function with three lists\n')
print(
   list( 
    zip(
        user_id,
        names,
        last_names
    )
   )
)

## more on zip
l1=[1,3,5,7]
l2=[2,4,6,8]

new_list =[max(pair) for pair in zip(l1,l2)]

print(new_list)

l=[(1,2),(3,4),(5,6),(7,8)]
print(*l)
print(
    list(
    zip(*l)
    )
)

l3,l4= list( zip(*l) )
print(l3,l4)