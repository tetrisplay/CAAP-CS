# Christina Tetrick
# Lab3

from random import randint

# global variable of chutes and ladders
# remenber to let your function know you're using this variable with 'global'
chutes_ladders = {4 : 7, 8 : 15, 12 : 2, 14: 6}

# Rolls a die of six sides and returns the result
def roll_die():
    return random.randint((1,6))
         
# makes a game (just a list) of the given dimensions
def makeGame(x, y):
    list = []
    for i in range((x*y)):
        list.append(i+1)
    print(list)

# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
    global chutes_ladders
    for i in chutes_ladders:
        if i == d:
            return True
    return False
      

# function to make and play a game
#Collaborated w/ Kevin Song
def play_game():
    option = input("What mode would you like to play in? 1 for player, 2 for computer: ")

    if option == 1:
        state = []
        global p
        p = int(input("How many people are playing?"))
    for i in range (p):
        playdiction.append({"state":1, "moves":0})
    makeGame(6,6)
    
    print(state)
    gameover = False
    while gameover == False:
        for player in range(p):
            print("Player", player+1, "is up next.")
            roll = input("Press any key to roll")
            die = roll_die()
            print("Player",player+1,"you rolled a",roll_die())
            state[player]['position'] += die
            state[player]['moves'] += 1
            if state[player]['position'] in chutes_ladders:
                state[player]['position'] = chutes_ladders[state[player]['position']]
            if state[player]['position'] > (6*6):
                gameover == True
                state[player]['position'] == 6*6
                print("player " + str(player +1) + ": you won!")
                print(state)
                break
    if option == 2:
        makeGame(6,6)
        position = 1
        moves = 0
        while position < (6*6):
            position += roll_die()
            moves += 1
            if position in chutes_ladders:
                position = chutes_ladders[position]
            if position == (6*6):
                break
            print(moves,"moves")

play_game()

#Sourced from jakevdp 
from random import Random
def simulate_game(rseed=None):
    
    rand = Random(rseed)
    position = 1
    turns = 0
    while position < 36:
        turns += 1
        roll = rand.randint(1,6)
        
        if position + roll > 36:
            continue
            
        position += roll
        
       
        position = chutes_ladders.get(position, position)
    return turns
