# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from gameComponents import gameVars, chooseWinner, comparison

while gameVars.player is False:	

	while gameVars.player_lives != 0 or gameVars.ai_lives != 0:

		print("■■■■■■■■■■■■■■■■■■ RPS BATTLE ■■■■■■■■■■■■■■■■■■")
		print("")
		print("=====================STATUS=====================")
		print("Player Health:", gameVars.player_lives, "/", gameVars.total_lives)
		print("    AI Health:", gameVars.ai_lives, "/", gameVars.total_lives)
		print("================================================")
		print("")
		print("⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⚒ARMOURY⚔⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘")
		print("         Rock✊    Scissors✌    Paper✋       ")
		print("       (You can only use one per a round)      ")
		print("⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘")
		print("")
		print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")	
		print("ARE YOU READY?! Btw type quit anytime to be a coward\n")
		# this is the player choice
		gameVars.player = input("Choose rock, paper or scissors: \n")
		
		# if player chose to quit, then exit the game
		if gameVars.player == "quit":
			print("Going somewhere?")
			exit()

		# player = true -> it has a value (rock, paper, or scissors)

		# this will be the AI choice -> a random pick from the choices array

		# check to see what the user input

		# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
		print("")
		print("The player strikes him with the " + gameVars.player + "!")

		# validate that the random choice worked for the AI
		# print("And AI brings up the " + computer + "!")
		# print("")

		comparison.comparison(gameVars.player)

		# --------- MOVE THIS CHUNK OF CODE TO A PACKAGE - START FROM HERE ------- #
		

		# -------------- STOP HERE - ALL OF THE ABOVE NEEDS TO MOVE --------------- #
		
		if gameVars.player_lives == 0:
			chooseWinner.winorlose("are better than that!")

		if gameVars.ai_lives == 0:
			chooseWinner.winorlose("just defeated me! How did you...?!")

		print("")
		print("You have", gameVars.player_lives, "drops of blood left.")
		print("AI has", gameVars.ai_lives, "drops of blood left.")
		print("")

		# make the loop keep running by setting player back to False
		# unset, so that our loop condition above will evaluate to True
		gameVars.player = False
