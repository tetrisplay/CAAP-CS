#GOOD FOR NOW
from random import randint

class Death(object):
	comments = ["You end up roaming the halls of Campus North forever, constantly wondering if you missed your 8 am Hume class.",
			"You bumped your head and died. Sorry.",
			"OH MY GOD ITS THE GHOST OF ROCHAFELLER! You die of fright.",
			"You accidently get locked into storage. I don't think anyone is going to save you.",
			"You stub your toe and crash into the vending machines, dieing from your injuries."
			]
	def enter(self):
		print (Death.comments[randint(0, len(self.comments)- 1)])
		return 'died'