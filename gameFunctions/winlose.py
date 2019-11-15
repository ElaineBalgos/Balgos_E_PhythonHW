from random import randint
from gameFunctions import gameWars

# define a python function that takes an argument
def winorloose(status):
	# status either won or lost - you're passing this is as an argument
	print("***********************************")
	print("*********  R P S G a m e  *********")
	print("***********************************")

	print("You", status,"! Would like to play again?")
	
	choice = input ("Y / N: ")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("You choose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		# reset the game so that we can start all over again
		# global player_lives
		# global computer_lives
		# global player
		# global computer
		# global choices

		gameWars.player_lives = 1
		gameWars.computer_lives = 1
		gameWars.total_lives = 1
		gameWars.player = False
		gameWars.computer = gameWars.choices[randint(0,2)]

	else:
		# use recursion to call winotlose again until we get the right input
		# recursion is just a fancy way to describe calling a function from within itself
		winlose.winorlose(status)