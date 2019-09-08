import vacuum
import time
queue = []

root = vacuum.create_root_node(10)
queue.append(root)
size = 0

while 1:
    temp = queue.pop(0)
    # temp_list = []
    # time.sleep(0.05)
    # if temp!=None:
    #     print(len(temp.previous_list))
    # if temp!=None and len(temp.previous_list) !=0:
    #     temp_list = temp.previous_list[:]
        # print(temp_list)
        # temp_list = list(dict.fromkeys(temp_list))
        # print(temp_list)
    # if temp!=None and len(temp.previous_list) !=0 and len(temp_list)!=len(temp.previous_list):
    #     temp = None
    if temp !=None:
        if temp.goal_test():
            print("found")
            print(temp.previous_list)
            exit()
        else:
            queue.append(temp.next_state("right"))
            queue.append(temp.next_state("left"))
            queue.append(temp.next_state("up"))
            queue.append(temp.next_state("down"))
            size+=1
            # print(size)




    
    
