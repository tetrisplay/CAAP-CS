#GOOD FOR NOW
from scores import Score

class Leaderboard(object):
	size = 10
	board = []

def __init__(self):
    for i in range(self.size):
        self.board.append(Score("player",i))

def print_board(self):
    print("High Scores: ")
    for entry in self.board:
        player = entry.get_name()
        score = entry.get_score()
        print(player + ":", score)

	# checks if given score should be in the leaderboard
def update(self, score):
    i = 0
    Newscore = score.get_score()
    Newname = score.get_name()
    for entry in self.board:
        if (score.get_score() >= entry.get_score()):
            self.board[i].set_score(Newscore)
            self.board[i].set_name(Newname)
            break
        i += 1

	