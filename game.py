# import the random package so that we can generate a random choice
from random import randint

# set up some variales for the player and AI Lives
player_lives = 5
computer_lives = 5

# choices is an array => a array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time
player = False

while player == False:
	#set player to True

	print("************************\n")
	print("Computer Lives:", computer_lives, "/5\n")
	print("Player Lives:", player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("************************\n")

	player = input("choose rock, paper or scissors: ")
	player = player.lower()

	print("computer choose", computer, "\n")
	print("player choose", player, "\n")

	if player.lower() == "quit":
		exit()

	elif computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if computer == "paper" :
			print("You lose!!!", computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You Win!!!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!!!", player, "covers", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!!!", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1

	else:
		print("That's not a valid choice, try again")

	# handle all lives list for player or AI
	if player_lives is 0:
		#reset the game so that we can start all over again
		print("Out of lives! You suck at this game. Would ypu like to play again?\n")
		choice = input ("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("You choose to quit.")
			exit()

		elif (choice is "Y") or (choice is "y"):
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choices[radint(0,2)]

	elif computer_lives is 0:
		print("Computer is out of lives! You suck at this game. Would you like to play again?\n")
		choice = input ("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("You choose to quit.")
			exit()

		elif (choice is "Y") or (choice is "y"):
			#reset the game so that we can start all over again
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choices[radint(0,2)]


	else: 
		# need ro check all if our conditions after checking for a tie
		player = False
		computer = choices[randint(0, 2)]

