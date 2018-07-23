class Engine(object):
    escaped = False
    lives = 3
    
    def __init__(self, scene_map): 
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        next_scene_name = ''
        checkpoint = ''
        n_moves = 0
        while (next_scene_name != 'finished' and self.lives > 0):
            print ("\n*******************************************************************") 
            next_scene_name = current_scene.enter()
            if (next_scene_name == ':q'):
                exit(1)
            elif (next_scene_name == 'death'):
                checkpoint = current_scene
                n_moves += 1
                current_scene = self.scene_map.next_scene(next_scene_name)
            elif (next_scene_name == 'died'):
                self.lives -= 1
                current_scene = checkpoint
            else:
                n_moves += 1
                current_scene = self.scene_map.next_scene(next_scene_name)
        if (next_scene_name == 'finished'):
            self.escaped = True
        return n_moves

def won(self):
    return self.escaped