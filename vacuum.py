import random
import sys
# import embed_graph
# side = embed_graph.tile_size
# def input_values(stri):
#     return int(input(stri))
side = int(input("Enter tile size:"))
tiles = side*side
temp_dirt = int(float(tiles*int(input("Enter dirt percentage:")))*(1/100))
if temp_dirt == 0:
    temp_dirt = 1
dirt = temp_dirt
# dirt = int(float(tiles*int(input("Enter dirt percentage:")))*(1/100)) + 1
# side = 4
# dirt = 2

class vacuum_node:
    def __init__(self, state, position = 0, previous_list = [], previous = None):
        self.state = state[:]
        self.previous_list = previous_list[:]
        self.position = position
        if (previous!=None):
            self.previous_list.append(previous)
        self.next_state("mop")
        # self.visit_list = visit_list[:]
        # self.visit_list[self.position] = 1


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
            if self.position%side == side - 1 or (self.position + 1) in self.previous_list:
                return None
            else:
                return vacuum_node(self.state, position = self.position + 1, previous_list = self.previous_list, previous = self.position)
        elif action == "left":
            if self.position%side == 0 or (self.position - 1) in self.previous_list:
                return None
            else:
                return vacuum_node(self.state, position = self.position - 1, previous_list = self.previous_list, previous = self.position)
        elif action == "up":
            if self.position//side == 0 or (self.position - side) in self.previous_list:
                return None
            else:
                return vacuum_node(self.state, position = self.position - side, previous_list = self.previous_list, previous = self.position)
        elif action == "down":
            if self.position//side == side - 1 or (self.position + side) in self.previous_list:
                return None
            else:
                return vacuum_node(self.state, position = self.position + side, previous_list = self.previous_list, previous = self.position)

class create_root_node(vacuum_node):
    def __init__(self, p):
        state = super().dirt_generator(p)
        super().__init__(state)
