# Christina Tetrick
# Lab3
#Heavy Collaboration w/ Kevin Song

from random import randint

# global variable of chutes and ladders
# remenber to let your function know you're using this variable with 'global'
chutes_ladders = {4 : 7,
					8 : 15,
					12 : 2,
					14 : 6}


# Rolls a die of six sides and returns the result
def roll_die():
    return randint(1,6)	

# makes a game (just a list) of the given dimensions
def makeGame(w, l):
    game_board = []
    for i in range((w*l)):
        game_board.append(i+1)
    print(game_board)
	
# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
    global chutes_ladders
    for i in chutes_ladders:
        if i == d:
            return True
        return False      
# function to make and play a game

def play_game():
    mode = input("What mode would you like to play in? 'p' for player, 'c' for computer automated: ")
        
    if mode == 'p':
        players = int(input("How many players?: "))
        state = []
        for i in range(players):
             state.append({'position':1,'moves':0})

        w = int(input("Enter a width: "))
        l = int(input("Enter a length: "))
        makeGame(w, l)


        print(state)
        gameover = False
        while gameover == False:
            for player in range(players):
                print("Player",player+1,"it is your turn")
                roll = input("Press any letter to roll the die: ")
                die = roll_die()
                print("Player",player+1,"you rolled a",roll_die())
                state[player]['position'] += die
                state[player]['moves'] += 1
                if state[player]['position'] in chutes_ladders:
                    state[player]['position'] = chutes_ladders[state[player]['position']]
                if state[player]['position'] > (w*l):
                    gameover == True
                    state[player]['position'] == w*l
                    print("player " + str(player +1) + ": you won!")
                    print(state)
                    break


    if mode == 'c':
        w = int(input("Enter a width: "))
        l = int(input("Enter a length: "))
        makeGame(w, l)
        position = 1
        moves = 0
        while position < (w*l):
            position += roll_die()
            moves += 1
            if position in chutes_ladders:
                position = chutes_ladders[position]
            if position == (w*l):
                break
        print(moves,"moves")

play_game()

#Sourced from jakevdp 
from random import Random
def simulate_game(rseed=None):
    
    rand = Random(rseed)
    position = 1
    turns = 0
    while position < w*l:
        turns += 1
        roll = rand.randint(1,6)
        
        if position + roll > w*l:
            continue
            
        position += roll
           
        position = chutes_ladders.get(position, position)
    return turns
