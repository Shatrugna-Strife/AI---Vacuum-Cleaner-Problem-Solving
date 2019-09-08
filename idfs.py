import vacuum
import time
import copy
queue = []

root = vacuum.create_root_node(15)
queue.append(root)
size = 0


def DFS(node):
    temp = copy.deepcopy(node)
    # temp = node
    if temp !=None:
        if temp.goal_test():
            print("found")
            print(temp.previous_list)
            exit()
    
    l = temp.next_state("left")
    if l!=None:
        # queue.append(l)
        # temp = DFS(l)
        DFS(l)
    r = temp.next_state("right")
    if r!=None:
        # queue.append(r)
        DFS(r)
    u = temp.next_state("up")
    if u!=None:
        # queue.append(u)
        DFS(u)
    d = temp.next_state("down")
    if d!=None:
        # queue.append(d)
        DFS(d)
    # return temp

DFS(root)