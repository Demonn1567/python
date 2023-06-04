#rock, paper, scissors game.
import random #importing an already defined library

def get_choices():  #defining a function
  player_choice = input("Enter a choice (rock,paper,scissors)")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player":player_choice, "computer":computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player} Computer chose {computer}")
  if player == computer :
    return "It's a tie!"
  elif player=="rock":
    if computer=="scissors":
      return "Rock smashes Scissors, you win!"
    else:
      return "Paper covers Rock, you lose."
  elif player=="paper":
    if computer=="rock":
      return "Paper covers Rock, you win!"
    else:
      return "Scissors cut Paper, you lose."
  elif player=="scissors":
    if computer=="paper":
      return "Scissors cut Paper, you win!"
    else:
      return "Rock smashes Scissors, you lose."
  

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)