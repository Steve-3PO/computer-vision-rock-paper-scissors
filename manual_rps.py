import random
import camera_rps

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

def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        print("It is a tie!")
        return "It is a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        return "You won!"
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        return "You won!"
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        return "You won!"
    else:
        print("You lost")
        return "You lost"
   
def play():
    pcwins, userwins = 0, 0
    while pcwins < 3 and userwins < 3: 
        computer_selected = get_computer_choice()
        user_selected = camera_rps.get_prediction()
        who_won = get_winner(user_selected, computer_selected)
        if who_won == "You won!":
            userwins += 1
        elif who_won == "You lost":
            pcwins += 1
    print("user wins") if userwins == 3 else print("pc wins")
play()
    
