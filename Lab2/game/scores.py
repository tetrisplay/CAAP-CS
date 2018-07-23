class Score(object):
    name = 'player'
    score = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
	
    def get_name(self):
	    return self.name
   
    def get_score(self):
	    return self.score
    
    def set_score(self, Newscore):
        self.score = Newscore
        
    def set_name(self, Newname):
        self.name = Newname
        
        