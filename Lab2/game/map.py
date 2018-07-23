#ADD IN EXTRA SCENES AS NEEDED
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter, 
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	scenes = {'dorm' : S.Dorm(),
				'basement' : S.Basement(),
				'ectoplasm' : S.Ectoplasm(),
				'hallway' : S.Hallway(),
				'laundry_room': S.Laundry_Room(),
				'finished': S.Finished()}
	
	# initializes to a starting scene
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	
	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene)
