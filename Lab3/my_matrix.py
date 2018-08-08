#Heavy help from Jesus with this section
#And I mean heavy help because I was struggling a lot
def make_matrix():
    r = int(input("What are your rows?"))
    c = int(input("What are your columns?"))
    a = [0]*r
    for i in range(r):
        a[i] = [0]*c
    print(a)
make_matrix()

# takes two matrices and multiplies them returnin the resulting matrix
def matrixmult():
    a = input("What is your first matrix?")
    b = input("What is your second matrix?")
    if len(a[0]) == len(b):
        product = make_matrix(len(a), len(b[0]))
    for i in range(len(product)):
        for j in range(len(product[0])):
            temp_variable = 0
            for n in range(len(b)):
                result = [i][j] + float(a[i][n]) * float(b[n][j])
        return result
    else:
        return []
    
matrixmult()

# prints the given matrix, mostly for testing purposes
def print_matrix(m):
    for i in range(len(m)):
        print(m[i])
        
print_matrix()

# given a state matrix, and a transition matrix, runs a markov simulation of the game and returns average number of moves.  
def markov_simulation(initial_matrix, transition_matrix, simulation_number):
    value = 0
    for i in range(simulation_number):
        loop = True
        moves = 0
        temporary_matrix = matrixmult(initial_matrix, transition_matrix)
        while loop == True:
            temp_matrix = matrixmult(temporary_matrix, transition_matrix)
            moves += 1
        if float(temporary_matrix[0][11]) > float(0.99):
            value += moves
            loop = False
    return float(value)/simulation_number
                         
                    
                    
                    
                    
	
