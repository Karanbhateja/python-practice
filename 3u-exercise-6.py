import random

guess_num = int(input("Enter the number between 1 and 100: "))
winning_num = random.randint(1, 100)
guess = 1
game_over=False
while not game_over:
    if guess_num == winning_num:
        print(f"You Win !!! and you guessed the answer in {guess} times")
        game_over=True
    elif winning_num > guess_num:
        print("Too Low")
        guess+=1
        guess_num=int(input("Guess Again : "))
    elif winning_num<guess_num:
        print("Too High")
        guess+=1
        guess_num=int(input("Guess Again : "))