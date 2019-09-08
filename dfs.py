import vacuum
import time
queue = []

root = vacuum.create_root_node(15)
queue.append(root)
size = 0


def DFS(node):
    temp = node
    if temp !=None:
        if temp.goal_test():
            print("found")
            print(temp.previous_list)
            exit()
    
    l = temp.next_state("left")
    if l!=None:
        # queue.append(l)
        temp = DFS(l)
    r = temp.next_state("right")
    if r!=None:
        # queue.append(r)
        temp = DFS(r)
    u = temp.next_state("up")
    if u!=None:
        # queue.append(u)
        temp = DFS(u)
    d = temp.next_state("down")
    if d!=None:
        # queue.append(d)
        temp = DFS(d)
    return temp

DFS(root)