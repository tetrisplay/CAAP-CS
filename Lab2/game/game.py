#GOOD FOR NOW
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ""
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
    global name
    global moves
    score = Score(name, moves)
    # ***************************************************
    # FIX You should only update if the won (goes inside the if statement)
    # *************************************************
    leaderboard.update(score)
    if (won):
        print("\nYou Won!") 
    leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name 
		global moves 
		print ("Welcome to The Mystery of Campus North! To quit enter :q at any time. You will have three lives. Good luck!") # raise ValueError ('todo')
		name = input("\nLet's play. Please enter your name. > ") # raise ValueError ('todo')
		if (name == ':q'):
			exit(1)
		a_map = Map('dorm') # raise ValueError ('todo')
		a_game = Engine(a_map)
		moves = a_game.play()
		game_over(a_game.won())

play_game()
