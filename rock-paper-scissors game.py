# rock-paper-scissors game.py
# This code implements a simple rock-paper-scissors game where the player can play against the computer. The player inputs their name and choice, and the computer randomly selects its choice. The game checks the winner based on the rules of rock-paper-scissors and allows the player to play multiple rounds until they choose to stop. The game also handles invalid inputs gracefully by prompting the player to try again.
# The game is designed to be user-friendly and interactive, providing feedback on each round and allowing the player to continue or exit as they wish. The use of functions helps to organize the code and make it more readable. The random module is used to generate the computer's choice, adding an element of unpredictability to the game. Overall, this code provides a fun and engaging way for players to enjoy a classic game while practicing their programming skills.


## Import the random module
import random

## Define the list of choices
list_of_choices = ["rock", "paper", "scissors"]
Player_name = input("Enter your name: ")

## Define the get_choice function
def get_choice():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  if player_choice not in list_of_choices:
    print("Invalid choice. Please try again.")
    return get_choice()
  computer_choice = random.choice(list_of_choices)
  print("Computer choice: " + computer_choice)
  print("Player choice: " + player_choice)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player_choice, computer_choice):
  if player_choice == computer_choice:
    print("It's a tie!")
  elif player_choice == "rock" and computer_choice == "scissors":
    print(Player_name + " is the winner!")
  elif player_choice == "paper" and computer_choice == "rock":
    print(Player_name + " is the winner!")
  elif player_choice == "scissors" and computer_choice == "paper":
    print(Player_name + " is the winner!")
  else:
    print("Computer is the winner!")

## Main game loop
while True:
  choice = get_choice()
  check_win(choice["player"], choice["computer"])
  
  play_again = input("Do you want to play again? (yes/no): ")
  if play_again.lower() != "yes":
    print("Thanks for playing!")
    break



## End of the game
