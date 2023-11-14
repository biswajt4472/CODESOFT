# A Sample Game For Rock,Paper,Seasor
import random


choices = ["Rock", "Paper", "Scissors"]
rules = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

user_score = 0
computer_score = 0


while True:

    user_choice = input("Enter your choice (Rock, Paper, Scissors) or E to quit: ").capitalize()
    if user_choice == "E":
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"Your choice : {user_choice}\nComputer choice : {computer_choice}.")
    if user_choice == computer_choice:
        print("It's a tie.")
    elif rules[user_choice] == computer_choice:
        print("You win!")
        user_score += 1
    else:
        print("You lose.")
        computer_score += 1
    print(f"Your score : {user_score}.\nComputer score : {computer_score}.")


print("Game over.")
print(f"Your final score : {user_score}.\nComputer's final score : {computer_score}.")
