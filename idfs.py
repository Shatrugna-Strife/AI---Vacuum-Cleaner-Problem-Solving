import vacuum
import time
import copy
queue = []

root = vacuum.create_root_node(5)
queue.append(root)


def DFS(node, depth = 0):
    temp = copy.deepcopy(node)
    # temp = node
    if temp !=None:
        if temp.goal_test():
            print("found")
            print(temp.previous_list)
            exit()
    
    l = temp.next_state("left")
    if l!=None and not depth<=0:
        # queue.append(l)
        # temp = DFS(l)
        DFS(l, depth = depth - 1)
    r = temp.next_state("right")
    if r!=None and not depth<=0:
        # queue.append(r)
        DFS(r, depth = depth - 1)
    u = temp.next_state("up")
    if u!=None and not depth<=0:
        # queue.append(u)
        DFS(u, depth = depth - 1)
    d = temp.next_state("down")
    if d!=None and not depth<=0:
        # queue.append(d)
        DFS(d, depth = depth - 1)
    # return temp
DFS(root, 15)