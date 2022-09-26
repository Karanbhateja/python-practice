name = "      Mr Robot      "
dots = "....."

print(name + dots)

print(name.lstrip() + dots)
# lstrip() method removes space from the left side.

print(name.rstrip() + dots)
# rstrip() method removes space from the right side.

print(name.strip() + dots)
# strip methos removes the space from both left and right side but nit from the centre.

# to remove the space from everywhere replace("what to replace" , "what to be replaced with") method can be used.
print(name.replace(" ", ""))