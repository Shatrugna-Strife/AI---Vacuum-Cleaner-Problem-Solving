import vacuum
import copy
queue = []

# root = vacuum.create_root_node(15)
# queue.append(root)
#
# stack = []
#
# def DFS(node, depth = 0):
#     temp = copy.deepcopy(node)
#     # temp = node
#     if temp !=None:
#         if temp.goal_test():
#             print("found")
#             print(temp.previous_list)
#             stack.append(temp.previous_list)
#
#             # for x in len(temp.visit_list):
#             #     if temp.visit_list[x] == 1:
#             #         print(x, end=" ")
#
#         l = temp.next_state("left")
#         if l!=None and not depth<=0 and len(stack) == 0:
#             # queue.append(l)
#             # temp = DFS(l)
#             DFS(l, depth = depth - 1)
#         r = temp.next_state("right")
#         if r!=None and not depth<=0 and len(stack)==0:
#             # queue.append(r)
#             DFS(r, depth = depth - 1)
#         u = temp.next_state("up")
#         if u!=None and not depth<=0 and len(stack)==0:
#             # queue.append(u)
#             DFS(u, depth = depth - 1)
#         d = temp.next_state("down")
#         if d!=None and not depth<=0 and len(stack)==0:
#             # queue.append(d)
#             DFS(d, depth = depth - 1)
#         # return temp
# DFS(root, 70)
# print(stack)


def i_d_f_s():
    root = vacuum.create_root_node(4)
    stack = []

    def DFS(node, depth = 0):
        temp = copy.deepcopy(node)
        # temp = node
        if temp !=None:
            if temp.goal_test():
                # print("found")
                # print(temp.previous_list)
                temp.previous_list.append(temp.position)
                stack.append(temp.previous_list)

                # for x in len(temp.visit_list):
                #     if temp.visit_list[x] == 1:
                #         print(x, end=" ")

            l = temp.next_state("left")
            if l!=None and not depth<=0 and len(stack) == 0:
                # queue.append(l)
                # temp = DFS(l)
                DFS(l, depth = depth - 1)
            r = temp.next_state("right")
            if r!=None and not depth<=0 and len(stack)==0:
                # queue.append(r)
                DFS(r, depth = depth - 1)
            u = temp.next_state("up")
            if u!=None and not depth<=0 and len(stack)==0:
                # queue.append(u)
                DFS(u, depth = depth - 1)
            d = temp.next_state("down")
            if d!=None and not depth<=0 and len(stack)==0:
                # queue.append(d)
                DFS(d, depth = depth - 1)
            # return temp
    DFS(root, 10)
    stack.append(root.state)
    return stack

new = i_d_f_s()
print(new)
