# To track the position in an iterable loop we can do it with for loop as follows - 
names = ['abc', 'abcd', 'abcde']
pos = 0 
for i in names:
  print(f"{pos}---> {i}")
  pos += 1

# Now doing same thing with enumerate function
for pos, name in enumerate(names):
  print(f"{pos}--->{name}")

# ----------------------PRACTICE-------------------------

