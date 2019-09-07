import sys
import random

class vacuum_node:
    def __init__(self, state, position = 0, previous = None):
        self.state = state[:]
        self.previous = []
        self.position = position
        if (previous!=None):
            self.previous.append(previous)
        self.next_state(self.state, "mop")
        
    
    def dirt_generator(self, p):
        tile = [0]*100
        num = random.sample(range(100), p)
        for i in num:
            tile[i] = 1
        return tile

    def goal_test(initial_state, goal_state):
        return initial_state == goal_state
    
    def next_state(self, state, action):
        if action == "mop":
            if self.state[self.position] == 1:
                self.state[self.position] = 0
        elif action == "right":
            if self.position%10 == 9:
                return None
            else:
                return vacuum_node(self.state, position = self.position + 1, previous = self.position)
        elif action == "left":
            if self.position%10 == 0:
                return None
            else:
                return vacuum_node(self.state, position = self.position - 1, previous = self.position)
        elif action == "up":
            if self.position//10 == 0:
                return None
            else:
                return vacuum_node(self.state, position = self.position - 10, previous = self.position)
        elif action == "down":
            if self.position//10 == 9:
                return None
            else:
                return vacuum_node(self.state, position = self.position + 10, previous = self.position)
        
class create_root_node(vacuum_node):
    def __init__(self, p):
        state = super().dirt_generator(p)
        super().__init__(state)






    

