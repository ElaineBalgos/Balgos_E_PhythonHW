# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameWars, compare

while gameWars.player is False:
	#set player to True
	print("************************\n")
	print("Computer Lives:", gameWars.computer_lives, "/", gameWars.total_lives, "\n")
	print("Player Lives:", gameWars.player_lives, "/", gameWars.total_lives, "\n")
	print("Choose your weapon!\n")
	print("************************\n")

	### this is where you would call compare
	gameWars.player = input("choose rock, paper or scissors:")
	gameWars.player = gameWars.player.lower()

	print("computer choose", gameWars.computer, "\n")
	print("player choose", gameWars.player, "\n")
	#how to pass arguments into a function

	if gameWars.player == "quit":
			print("Thank you for playing, Bye!")
	elif gameWars.player == gameWars.computer:
			compare.comparechoices("computer", "player")
	elif gameWars.player != gameWars.computer:
			compare.comparechoices("computer", "player")	
	else:
			print("Ow oh..That's not a valid choice, Try again!")
			gameWars.player = False
			gameWars.computer = gameWars.choices[randint(0,2)]
 
	### end compare stuff

	# handle all lives list for player or AI
	if gameWars.player_lives is 0:
		winlose.winorloose("lost")
		
		# print("Out of lives! You suck at this game. Would you like to play again?\n")
		# choice = input ("Y / N")
		# print(choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("You choose to quit.")
		# 	exit()

		# elif (choice is "Y") or (choice is "y"):
		# 	player_lives = 5
		# 	gameWars.computer_lives = 5
		# 	player = False
		# 	gameWars.computer = choices[radint(0,2)]

	elif gameWars.computer_lives is 0:
		winlose.winorloose("won")
				# print("gameWars.computer is out of lives! You suck at this game. Would you like to play again?\n")
		# choice = input ("Y / N")
		# print(choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("You choose to quit.")
		# 	exit()

		# elif (choice is "Y") or (choice is "y"):
		# 	#reset the game so that we can start all over again
		# 	player_lives = 5
		# 	gameWars.computer_lives = 5
		# 	player = False
		# 	gameWars.computer = choices[radint(0,2)]


	else: 
		# need to check all if our conditions after checking for a ties
		player = False
		gameWars.computer = gameWars.choices[randint(0, 2)]

