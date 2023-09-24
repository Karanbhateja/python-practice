# Check if any element is present in set or not using 'in' keyword
set1 = {'a','b','c'}
# We can use 'in' keyword with if a same in List and Tupple
if 'c' in set1:
  print("Present")
else:
  print("Not Present")

# Iteration in Sets (For Loop)
for items in set1:
  print(items) # There will be no fixed order of printing the elements of the set, because it is unordered collection of elements/ So every time the order of printing will be deifferent

# SET MATHS (Union and Intersection)

s1 = {1,2,3,4}
s2 = {3,4,5,6}

# Union
union_set = s1 | s2 # For unio we use | (pipe)
print(union_set) # Output - {1,2,3,4,5,6}

# Intersection
intersection_set = s1 & s2 # For intersection we use & 
print(intersection_set)
