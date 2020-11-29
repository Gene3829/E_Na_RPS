from gameComponents import gameVars, chooseWinner, comparison
from random import randint

# define comparison function
def comparison(status):
	# print("inside winorlose function; status is: ", status)
	computer = gameVars.choices[randint(0, 2)]

	print("And AI brings up the " + computer + "!")
	print("")	

	if (computer == gameVars.player):
			print("How fierce, you two!")
		# always check for negative conditions first (the losing case)

	elif (computer == "scissors"):
		if  (gameVars.player == "rock"):			
			print("You just crushed the scissors in half!!")
			gameVars.ai_lives -= 1
		else:
			print("Oh, man... Are you ok..?")
			gameVars.player_lives -= 1	

	elif (computer == "paper"):
		if  (gameVars.player == "scissors"):
			print("Woah..! That's ruthless!!")
			gameVars.ai_lives -= 1
		else:
			print("Yep, that could have worked but...")
			gameVars.player_lives -= 1

	elif (computer == "rock"):
		if  (gameVars.player == "paper"):
			print("Paper brutally compresses rock!!")
			gameVars.ai_lives -= 1
		else:
			print("Oof...")
			gameVars.player_lives -= 1
		