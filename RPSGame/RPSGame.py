import random

def get_choices():
	player_choice = input("Let's play a game of rock, paper, scissors! Choose your pick! ")
	rps = ["rock", "paper", "scissors"]
	computer_choice = random.choice(rps)
	choices = {"player": player_choice, "computer": computer_choice}
	return choices

def check_win(player, computer):
	print(f"You chose {player}, and the computer chose {computer}")
	if player == computer:
		return "It's a tie."
	elif player == "rock":
		if computer == "paper":
			return "Paper covers rock. You lose. :("
		else:
			return "Rock smashes scissors. You win! :D"
	elif player == "scissors":
		if computer == "paper":
			return "Scissors cuts paper. You win! :)"
		else:
			return "Rock smashes scissors. You lose. :,("
	else:
		if computer == "rock":
			return "Paper covers rock. You win! :)"
		else:
			return "Scissors cuts paper. You lose. :/"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
	
