class Scene(object):

	# This is wrong, should be the original, no need to change anything here
	# ****************************************
    def __init__(enter, action, exit_scene):
        print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
        print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
        exit(1)
    # ****************************************

    # This works fine
    def enter(self):
    	print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
    	print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
    	exit(1)

class Dorm(Scene):
    
    name = 'dorm' 

    def enter(self):
	    print ("You are in your dorm, and you here a knock on your door.")
	    raise ValueError ('Sorry for the error!')
	    return self.action()

    def action(self):
	    print ("What will you do? Option 1: Go to your door. Option 2: lay down and nap. Please enter a number.")
	    raise ValueError ('There was an error!')
	    choice = input("> ")
	    if choice == ':q':
	        return self.exit_scene(choice)
			# this is some exception handling, you don't need to worry about it, 
			# just accept that it works and keeps the program from falling apart.
	    try:
	        choice = int(choice)
	    except ValueError:
	        print("That's not an int!")
	        return self.exit_scene(self.name)

	    if int(choice) == 1:
	        print ("You are taken by a mysterious force to an unknown location.")
	        raise ValueError ('Sorry for the error!')
	        return self.exit_scene('basement') # raise ValueError ('todo')
	    elif int(choice) == 2:
	        print ("You are taken by a mysterious force to an uknown location.")
	        raise ValueError ('Sorry for the error!')
	        return self.exit_scene('basement') # raise ValueError ('todo')
	    else:
	        print ("Not a valid option. Choose an option or type :q to end game") 
	        return self.exit_scene(self.name)

    def exit_scene(self, outcome):
        return outcome

class Basement(Scene):
	
	name = 'basement'

	def enter(self):
		print ("You appear to be in the basement of Campus North. You do not have access to the elevator or stairs. You can't see right now because there is no light.")
		raise ValueError ('Sorry for the error')
		return self.action()

	def action(self):
		print ("What will you do? Option 1: Use your phone as a flashlight. Option 2: Boldly walk around without a light; you do live in this dorm after all. Option 3: Lay down and cry. Please enter a number.")
		raise ValueError ('There was an error!')
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not a number.")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You see a strange ectoplasm on the floor. It's really reflective, and you are quite curious. You think it best to explore where it leads.")
			raise ValueError ('Sorry for the error!')
			return self.exit_scene('ectoplasm') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("You walk around the basement, absolutely confident in your ability to navigate the dark.")
			raise ValueError ('Sorry for the error!')
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print("This is all just too much. Overwelmed, you decide to lay down and cry on the floor.")
			raise ValueError ('Sorry for the error!')
			return self.exit_scene('hallway')
		else:
			print ("Not a valid option. Choose an option or type :q to end game") 
			print ("But if you do, you will never solve The Mystery of Campus North.")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
    
class Ectoplasm(Scene):
	
	name ='ectoplasm'

	def enter(self):
		print ("You have decided to explore where the ectoplasm leads. You see that the trail leads to the laundry room. It's quite ominous.")
		raise ValueError ('Sorry about the error!')
		return self.action()
	
	def action(self):
		print("What will you do? Option 1: Follow the ectoplasm. Option 2: Run in fear.")
		raise ValueError ('There was an error!')
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		 
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not a number.")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You follow the ectoplasm and arrive in the laundry room, sensing something is wrong.")
			raise ValueError ('Sorry for the error!')
			return self.exit_scene('laundry_room') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("You run away in fear, terrified of all the events that have occured.")
			raise ValueError ('Sorry for the error!')
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("Not a valid option. Choose an option or type :q to end game") 
			print ("But if you do, you will never solve The Mystery of Campus North.")  
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Hallway(Scene):
	
	name = 'hallway'

	def enter(self):
		("After lying down and crying on the floor, wondering about the meaning of your life, you see a lost CAAP student walking towards you. He looks tired, overworked, and just really stressed.")
		raise ValueError ('There was an error!')
		return self.action()

	def action(self):
		print("What will you do? Option 1: Ignore the student. Option 2: Follow the student. Option 3: Have the student follow you.")
		raise ValueError ('There was an error!')
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		 
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not a number.")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You ignore the student and consider become a nihilist, for all of life pretty much pointless.")
			raise ValueError ('Sorry for the error!')
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("You follow the student. Neither of you talk. You wonder how this all will end.")
			raise ValueError ('Sorry for the error!')
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print("You convince the student that you know how to get out of this situation. During your converstation, you spot a strange ectoplasm. You decide to follow it and abandon the CAAP student.")
			raise ValueError ('Sorry for the error!')
			return self.exit_scene('ectoplasm')
		else:
			print ("Not a valid option. Choose an option or type :q to end game") 
			print ("But if you do, you will never solve The Mystery of Campus North.")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Laundry_Room(Scene):
    
    name = 'laundry_room'

    def enter(self):
    	print ("You enter the laundry room, and inside you see a pile of cloths waiting to be washed. They smell pretty bad.")
    	raise ValueError ('There was an error!')
    	return self.action()

    def action(self):
    	print("What will you do? Option 1: Do laundry. Option 2: Look through the clothes. Option 3: Ignore the pile of clothes and see what else is in the laundry room.")
    	raise ValueError ('There was an error!')
    	choice = input("> ")
    	if choice == ':q':
    		return self.exit_scene(choice)

    	try:
    		choice = int(choice)
    	except ValueError:
    		print("That's not a number.")
    		return self.exit_scene(self.name)

    	if int(choice) == 1:
    		print ("You decide to do laundry. As you are washing the clothes, you see a ghOST OH MY GOD ITS COMING FOR YOU.")
    		raise ValueError ('Sorry about the error!')
    		return self.exit_scene('death') # raise ValueError ('todo')
    	elif int(choice) == 2:
    		print ("As you look through the clothes, you stumble upon Dean Boyer. He hands you a check covering four years of tuition. You are happy yet unsure of how to handle the future implications of this money.")
    		raise ValueError ('Sorry for the error!')
    		return self.exit_scene('finished') # raise ValueError ('todo')
    	elif int(choice) == 3:
            print("As you look around, everything starts to fade from view. You wake up in your dorm, realizing this was all just a dream.")
            raise ValueError ('Sorry for the error!')
            return self.exit_scene('finished')
    	else:
        	print ("Not a valid option. Choose an option or type :q to end game") 
        	print ("But if you do, you will never solve The Mystery of Campus North.")
        	return self.exit_scene(self.name)

    def exit_scene(self, outcome):
    	return outcome
    
class Finished(Scene):
    
    name = 'finished'
    
    def enter(self):
        print("Congratulations! You have solved The Mystery of Campus North!")
        return self.exist_scene('finished')
    
    def exit_scene(self, outcome):
    	return outcome
    

		
