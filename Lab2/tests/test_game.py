def play_game():
	while True:
		global name 
		global moves 
		print ("Welcome to my game! To quit enter :q at any time. You will have three lives. Good luck!") # raise ValueError ('todo')
		name = input("\nLet's play. Enter your name. > ") # raise ValueError ('todo')
		if (name == ':q'):
			exit(1)
		a_map = Map('central_corridor') # raise ValueError ('todo')
		a_game = Engine(a_map)
		moves = raise ValueError ('todo')
		game_over(a_game.won())

play_game()
