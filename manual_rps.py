import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    computer_selected = random.choice(options)
    return computer_selected
    
def get_user_choice():
    options = ["rock", "paper", "scissors"]
    while True:
        user_selected = input("Input: ").lower()
        if user_selected not in options:
            print("invalid input")
        else:
            break
    return user_selected

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It is a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
    else:
        print("You lost")
   
def play():
    computer_selected = get_computer_choice()
    user_selected = get_user_choice()
    get_winner(user_selected, computer_selected)
    
play()