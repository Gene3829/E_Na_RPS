from gameComponents import gameVars

# define a win or lose function
def winorlose(status):
	# print("inside winorlose function; status is: ", status) 
	
	print("You", status, "Want another battle?!")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("")
		print("Fine! I'll see you next time then...!")
		exit()

	elif choice == "Y" or choice == "y":
		# reset the player lives and the AI lives
		# and set player to False so that our loop will restart		
		
		print("")
		print("Good! You and me, again!")
		gameVars.player_lives = 5
		gameVars.ai_lives = 5
		gameVars.player = False


	else:
		print("I won't ask you the second time...! - Y or N?!")
		# this will generate a bug that we need to fix later
		choice = input("Y / N: ")