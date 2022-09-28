win_number = 15
guess_number = int(input("Guess the number : "))

if guess_number==win_number:
    print("You win !!!")
    
else:             # Nested if else
    if guess_number>win_number:
        print("Your guess is higher than the answer")
    else: # You can also use if here.
        print("Your guess is lower than the answer")