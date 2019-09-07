import vacuum 
queue = []

root = vacuum.create_root_node(15)
queue.append(root)
size = 0

while queue:
    temp = queue.pop(0)
    if temp !=None:
        if temp.goal_test():
            print("found")
            # print(size)
            exit()
        else:
            queue.append(temp.next_state("right"))
            queue.append(temp.next_state("left"))
            queue.append(temp.next_state("up"))
            queue.append(temp.next_state("down"))
            size+=1
            # print(size)




    
    
