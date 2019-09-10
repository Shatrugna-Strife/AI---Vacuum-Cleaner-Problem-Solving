import vacuum
import copy
import time
queue = []


def i_d_f_s(root_node):
    # root = vacuum.create_root_node(vacuum.dirt)
    root = root_node
    stack = []
    value = [0, 1]
    t1 = time.time()
    # depth = 0
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
            tw = value.pop()
            value.append(tw+1)
            if l!=None and not depth<=0 and len(stack) == 0:
                # queue.append(l)
                # temp = DFS(l)
                DFS(l, depth = depth - 1)
            r = temp.next_state("right")
            tw = value.pop()
            value.append(tw+1)
            if r!=None and not depth<=0 and len(stack)==0:
                # queue.append(r)
                DFS(r, depth = depth - 1)
            u = temp.next_state("up")
            tw = value.pop()
            value.append(tw+1)
            if u!=None and not depth<=0 and len(stack)==0:
                # queue.append(u)
                DFS(u, depth = depth - 1)
            d = temp.next_state("down")
            tw = value.pop()
            value.append(tw+1)
            if d!=None and not depth<=0 and len(stack)==0:
                # queue.append(d)
                DFS(d, depth = depth - 1)
            # return temp
    for i in range(vacuum.side*vacuum.side*2):
        if len(stack)==0:
            DFS(root, i)
        else:
            value[0] = i
            break

    # DFS(root, 50)
    stack.append(root.state)
    stack.append(value)
    stack.append([-(t1-time.time())])
    print(stack)
    # print(len(stack[1]))
    return stack

# i_d_f_s()
