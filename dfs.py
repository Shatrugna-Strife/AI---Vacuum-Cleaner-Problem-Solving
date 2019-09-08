import vacuum
import copy


queue = []

root = vacuum.create_root_node(5)
queue.append(root)
size = 0
stack = []
temp = root

while queue:
    if temp !=None:
        if temp.goal_test():
            stack.append(temp.previous_list)
            break
        l = temp.next_state("left")
        if l!=None:
            queue.append(l)
            temp = l
            continue
        r = temp.next_state("right")
        if r!=None:
            queue.append(r)
            temp = r
            continue
        u = temp.next_state("up")
        if u!=None:
            queue.append(u)
            temp = u
            continue
        d = temp.next_state("down")
        if d!=None:
            queue.append(d)
            temp = d
            continue
    temp = queue.pop()
# min = stack.pop(0)
# for i in stack:
#     if len(min) > len(i):
#         min = i[:]
print(stack)

