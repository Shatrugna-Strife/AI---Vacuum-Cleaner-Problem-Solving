import sys
import random
side = 10
tiles = side*side

class vacuum_node:
    def __init__(self, state, position = 0, previous = None):
        self.state = state[:]
        self.previous = []
        self.position = position
        if (previous!=None):
            self.previous.append(previous)
        self.next_state("mop")
        
    
    def dirt_generator(self, p):
        tile = [0]*tiles
        num = random.sample(range(tiles), p)
        for i in num:
            tile[i] = 1
        return tile

    def goal_test(self):
        temp_state = [0]*tiles
        # for i in range(len(self.state)):
        #     if self.state[i]!=temp_state:
        #         return False
        # return True
        return self.state == temp_state 

    def next_state(self, action):
        if action == "mop":
            if self.state[self.position] == 1:
                self.state[self.position] = 0
        elif action == "right":
            if self.position%side == side - 1:
                return None
            else:
                return vacuum_node(self.state, position = self.position + 1, previous = self.position)
        elif action == "left":
            if self.position%side == 0:
                return None
            else:
                return vacuum_node(self.state, position = self.position - 1, previous = self.position)
        elif action == "up":
            if self.position//side == 0:
                return None
            else:
                return vacuum_node(self.state, position = self.position - side, previous = self.position)
        elif action == "down":
            if self.position//side == side - 1:
                return None
            else:
                return vacuum_node(self.state, position = self.position + side, previous = self.position)
        
class create_root_node(vacuum_node):
    def __init__(self, p):
        state = super().dirt_generator(p)
        super().__init__(state)






    

