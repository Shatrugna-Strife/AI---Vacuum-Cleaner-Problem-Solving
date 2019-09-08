import vacuum
queue = []

root = vacuum.create_root_node(1)
queue.append(root)
stack = []
size = 0

while queue:
    temp = queue.pop(0)

    # time.sleep(0.05)

    if temp !=None:
        if temp.goal_test():
            print("found")
            print(temp.previous_list)
            stack.append(temp.previous_list)
        else:
            queue.append(temp.next_state("right"))
            queue.append(temp.next_state("left"))
            queue.append(temp.next_state("up"))
            queue.append(temp.next_state("down"))

print(stack)
# i = queue.pop()
# print(i.previous_list)