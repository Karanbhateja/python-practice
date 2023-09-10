# Sets is a unordered collection of unique items. There cannot be 2 same values in a set.
# It is created by using Curly Braces {} Dictionary is also created by using same braces but in sets there is no Key Value pair like Dictionary
# A set can store Number, String, Floating Point Values but not List, Dictionary, tupple or another set.

s = {1,2,3,2}
print(s) 
# This will print {1,2,3} as there are only unique values in Sets.
# Also there is no indexing available in sets as it is unordered collection

# Sets can also be used to remove dupllicate elements from the list for example -

listex = [1,2,2,2,2,3,3,3,4,4,4,4,5,5,6,6,6,6,7,7,7,7,7,7]
s2 = set(listex)
# Output - {1,2,3,4,5,6,7}

listex = list(s2) # Converting back to the list
# Output - [1,2,3,4,5,6,7]

# Adding Items to the Set (Add Method)
s.add(4)
print(s) # Output - {1,2,3,4}

#  Removing elelment form Set (Remove Method & Discard Method)
s.remove(3)
print(s) # Output - {1,2,4}

s.remove(20) # If we use remove method on an element which is not present in the set then it will give an error
s.discard(20) # But if we use discard mwthod wiht an element which does not exist in a set then it will niether give an error nor it will remove any other element.

# Clearing the whole set (Clear Method)
s.clear() 

# Copying a Set (Copy Method)
s1 = s.copy()
