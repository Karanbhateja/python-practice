# Break is used to completely break the loop when a certain condition is matched.

for i in range(11):
    if i ==5:
        break # As the value of i reaches 5 this will met the condition and will break the loop.
    print(i)

print("\n")

# Continue can be used to skip a output on certain condition.

for i in range(11):
    if i ==5:
        continue # This will skip the output and will return to the for loop without comleting the pront action.
    print(i)