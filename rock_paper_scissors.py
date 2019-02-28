#Rock Paper Scissors Game!
#Simple python game using some conditional & logical structure and random module.

import random
print ("******************************\n\n")
print ("Rock Paper Scissors Game!\n\n")
print ("1. Player vs Player   2. Player vs Computer \n\n")

choice = input("Choose mode 1 or 2: ")

if int(choice) == 1:

	p1 = input("Player's 1 move: ")
	print("**** HIDING PLAYER'S 1 MOVE ****\n\n" * 20)
	p2 = input("Player'2 move: ")
	print ("Player's 1 move was: " + str(p1)) 

	if p1 == p2:
	    print("Draw!\n")
	elif p1 == "rock" and p2 == "scissors":
	    print("Player 1 win!")
	elif p1 == "paper" and p2 == "rock":
	    print("Player 1 win!")
	elif p1 == "rock" and p2 == "paper":
	    print("Player 1 win!")
	else:
	    print("Player 2 win!")

else:
	ai_move = random.choice(["paper", "rock", "scissors"])
	player_move = input("Computer has moved... Now your move rock, paper or scissors:  ")
	print ("Computer's move was " + str(ai_move))
	if ai_move == player_move:
	    print("Draw!\n")
	elif ai_move == "rock" and player_move == "scissors":
	    print("You lost :(")
	elif ai_move == "paper" and player_move == "rock":
	    print("You lost :(")
	elif ai_move == "scissors" and player_move == "paper":
	    print("You lost :(")
	else:
	    print("Great! You won!")





