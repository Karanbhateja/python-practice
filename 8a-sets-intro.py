# Sets is a unordered collection of unique items. There cannot be 2 same values in a set.
# It is created by using Curly Braces {} Dictionary is also created by using same braces but in sets there is no Key Value pair like Dictionary

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
