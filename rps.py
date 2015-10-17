import random
# You must make a rock paper scissors game
# Goal
# Ask the player if they pick rock paper or scissors
# Have the computer chose its move
# Compare the choices and decide who wins
# Print the results
# Subgoals
# Let the player play again

# This code is written in a very basic, simplistic manner so it is easy for new programmers to understand

moves = ["rock","paper","scissors"]

def take_input():
	choice = raw_input("Rock, Paper, or Scissors?: ")
	choice = choice.lower()
	return choice

def computer_move():
	return moves[random.randint(0,2)]

# 0 is draw
# 1 is user win
# 2 is computer win
def winner(user_move, computer_move):
	if(user_move == "rock"):
		if(computer_move == "rock"):
			return "draw"
		if(computer_move == "paper"):
			return "computer"
		if(computer_move == "scissors"):
			return "user"

	if(user_move == "paper"):
		if(computer_move == "rock"):
			return "user"
		if(computer_move == "paper"):
			return "draw"
		if(computer_move == "scissors"):
			return "computer"

	if(user_move == "scissors"):
		if(computer_move == "rock"):
			return "computer"
		if(computer_move == "paper"):
			return "user"
		if(computer_move == "scissors"):
			return "draw"

def better_print(outcome):
	if(outcome == "computer"):
		print "You lose!"
	if(outcome == "user"):
		print "You win!"
	if(outcome == "draw"):
		print "It's a draw!"

def print_score(user_score, computer_score):
	print ("The score is %s to %s" %(user_score, computer_score))

def play_again():
	decision = raw_input("Do you want to play again?: ")
	decision = (decision[:1]).lower()

	if(decision == "y"):
		return True
	else:
		return False

def play_game():
	keep_playing = True
	user_score = 0
	computer_score = 0
	while(keep_playing):
		user_choice = take_input()
		computer_choice = computer_move()
		outcome = winner(user_choice, computer_choice)
		if(outcome == "user"):
			user_score += 1
		if(outcome == "computer"):
			computer_score += 1
		better_print(outcome)
		print_score(user_score, computer_score)
		keep_playing = play_again()
	print "Thanks for playing!"

#MAIN	
play_game()




