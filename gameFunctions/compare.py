from random import randint
from gameFunctions import compare, winlose, gameWars
# what are you trying to compare inside this function?
# you will need to pass those things in as arguments
# inside the round brackets
def comparechoices(computer, player):

	if gameWars.player == "quit":
		exit()

	elif gameWars.computer == gameWars.player:
		print("Tie! no one wins, play again :)")
	
	elif gameWars.player != gameWars.computer:
		if gameWars.player == "rock":
			if gameWars.computer == "paper":
				print("Sad, You Lose...", gameWars.computer, "covers", gameWars.player, "\n")
				gameWars.player_lives = gameWars.player_lives - 1
			else:
				print("Wohoo!!! You Win!", gameWars.player, "smashes", gameWars.computer, "\n")
				gameWars.computer_lives = gameWars.computer_lives - 1

		elif gameWars.player == "paper":
			if gameWars.computer == "scissors":
				print("Sad, You Lose...", gameWars.computer, "cuts", gameWars.player, "\n")
			else:
				print("Wohoo!!! You Win!", gameWars.player, "smashes", gameWars.computer, "\n")

		elif gameWars.player == "scissors":
			if gameWars.computer == "rock":
				print("Sad, You Lose...", gameWars.computer, "smashes", gameWars.player, "\n")
			else:
				print("Wohoo!!! You Win!", gameWars.player, "cuts", gameWars.computer, "\n")

		elif gameWars.player != gameWars.choices[randint(0,2)]:
			if gameWars.computer == gameWars.choices[randint(0,2)]:
				print("Ow oh..That's not a valid choice!!!")
			else:
				print("Ow oh..That's not a valid choice!!!")

	gameWars.player = False
	gameWars.computer = gameWars.choices[randint(0,2)]