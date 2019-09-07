import random

def dirt_generator(p):
    tile = [0]*100
    num = random.sample(range(100), p)
    for i in num:
        tile[i] = 1
    return tile

# tile = dirt_generator(10)

def goal_test(initial_state, goal_state):
    # for i in range(len(initial_state.tile)):
    #     if (initial_state.tile[i] == goal_state.tile[i]):
    #         pass
    #     else:
    #         return False
    # return True
    return initial_state == goal_state

# print(goal_test(tile, [0]*100))
