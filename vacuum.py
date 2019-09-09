import random
import sys
side = 7
tiles = side*side

# class vacuum_node:
#     def __init__(self, state, position = 0, previous_list = [], visit_list= [0]*tiles, previous = None):
#         self.state = state[:]
#         self.previous_list = previous_list[:]
#         self.position = position
#         if (previous!=None):
#             self.previous_list.append(previous)
#         self.next_state("mop")
#         self.visit_list = visit_list[:]
#         self.visit_list[self.position] = 1
#
#
#     def dirt_generator(self, p):
#         tile = [0]*tiles
#         num = random.sample(range(tiles), p)
#         for i in num:
#             tile[i] = 1
#         return tile
#
#     def goal_test(self):
#         temp_state = [0]*tiles
#         # for i in range(len(self.state)):
#         #     if self.state[i]!=temp_state:
#         #         return False
#         # return True
#         return self.state == temp_state
#
#     def next_state(self, action):
#         if action == "mop":
#             if self.state[self.position] == 1:
#                 self.state[self.position] = 0
#         elif action == "right":
#             if self.position%side == side - 1 or self.visit_list[self.position + 1] == 1:
#                 return None
#             else:
#                 return vacuum_node(self.state, position = self.position + 1, previous_list = self.previous_list, visit_list = self.visit_list, previous = self.position)
#         elif action == "left":
#             if self.position%side == 0 or self.visit_list[self.position - 1] == 1:
#                 return None
#             else:
#                 return vacuum_node(self.state, position = self.position - 1, previous_list = self.previous_list, visit_list = self.visit_list, previous = self.position)
#         elif action == "up":
#             if self.position//side == 0 or self.visit_list[self.position -side] == 1:
#                 return None
#             else:
#                 return vacuum_node(self.state, position = self.position - side, previous_list = self.previous_list, visit_list = self.visit_list, previous = self.position)
#         elif action == "down":
#             if self.position//side == side - 1 or self.visit_list[self.position + side] == 1:
#                 return None
#             else:
#                 return vacuum_node(self.state, position = self.position + side, previous_list = self.previous_list, visit_list = self.visit_list, previous = self.position)

# class create_root_node(vacuum_node):
#     def __init__(self, p):
#         state = super().dirt_generator(p)
#         super().__init__(state)

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


# state = [0]*100
# g = vacuum_node(state)
# print(sys.getsizeof(g))
# for _ in range(7):
#     g = g.next_state("right")
# g = g.next_state("right")
# g = g.next_state("right")
# g = g.next_state("down")
# g = g.next_state("left")
# g = g.next_state("up")
# print(g.previous_list)
# g = g.next_state("down")
# f = g.next_state("right")
# f = f.next_state("right")
# print(id(f.previous_list))
# print(id(g.previous_list))
# print(g.previous_list)
# print(f.previous_list)
# print (g.previous_list)
