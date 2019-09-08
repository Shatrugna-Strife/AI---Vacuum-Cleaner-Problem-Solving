import vacuum
import copy
queue = []

# root = vacuum.create_root_node(5)
# queue.append(root)
# size = 0
# stack = []
# temp = root
# depth = 1

# while queue:
#     if temp !=None:
#         if temp.goal_test():
#             stack.append(temp.previous_list)
#             break
#         l = temp.next_state("left")
#         if l!=None and not depth < 0:
#             queue.append(l)
#             temp = l
#             depth -=1
#             continue
#         r = temp.next_state("right")
#         if r!=None and not depth < 0:
#             queue.append(r)
#             temp = r
#             depth -=1
#             continue
#         u = temp.next_state("up")
#         if u!=None and not depth < 0:
#             queue.append(u)
#             temp = u
#             depth -=1
#             continue
#         d = temp.next_state("down")
#         if d!=None and not depth < 0:
#             queue.append(d)
#             temp = d
#             depth -=1
#             continue
#     temp = queue.pop()
#     depth += 1
# print(stack)


root = vacuum.create_root_node(1)
queue.append(root)

stack = []

def DFS(node, depth = 0):
    temp = copy.deepcopy(node)
    # temp = node
    if temp !=None:
        if temp.goal_test():
            print("found")
            print(temp.previous_list)
            stack.append(temp.previous_list)
            # for x in len(temp.visit_list):
            #     if temp.visit_list[x] == 1:
            #         print(x, end=" ")

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
DFS(root, 19)
print(stack)
