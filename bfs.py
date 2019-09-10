import vacuum
import time

def b_f_s(root_node):
    t1 = time.time()
    queue = []
    root = root_node
    # root = vacuum.create_root_node(vacuum.dirt)
    queue.append(root)
    stack = []
    size = [1, 1]

    while queue:
        temp = queue.pop(0)
        size[0] -= 1
        # time.sleep(0.05)

        if temp !=None:
            # size[0] +=1
            # size[1] += 1
            if temp.goal_test():
                print("found")
                print(temp.previous_list)
                temp.previous_list.append(temp.position)
                stack.append(temp.previous_list)
                break
            else:
                queue.append(temp.next_state("right"))
                queue.append(temp.next_state("left"))
                queue.append(temp.next_state("up"))
                queue.append(temp.next_state("down"))
                size[0] +=4
                size[1] += 4
    queue =None
    stack.append(root.state)
    stack.append(size)
    stack.append([-(t1 - time.time())])
    print(stack)
    return stack


# b_f_s()
# i = queue.pop()
# print(i.previous_list)
# queue = []
