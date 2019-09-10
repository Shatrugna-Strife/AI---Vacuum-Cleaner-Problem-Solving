import tkinter
import random
from PIL import ImageTk, Image
import time
import idfs
import bfs
import math
import vacuum

# master = tkinter.Tk()
# canvas = tkinter.Canvas(master, width = 1500, height = 800)


def grid_1(master, canvas, canvas2, root_node, value):
    # stack = idfs.i_d_f_s(root_node)
    # print(stack)


    grid_1_size = 50
    rectangle_1_x = 10
    rectangle_1_y = 10

    image_size = 50
    vacuum_pos_x = image_size/2
    vacuum_pos_y = image_size/2
    size = vacuum.side

    grid_2_size = 50
    rectangle_2_x = rectangle_1_x + size*grid_1_size + grid_2_size
    rectangle_2_y = rectangle_1_y

    # master = tkinter.Tk()
    # canvas = tkinter.Canvas(master, width = 1500, height = 800)
    img_1 = ImageTk.PhotoImage(Image.open("dirt.jpg"))
    img_2 = ImageTk.PhotoImage(Image.open("vacuum.jpg"))
    img_3 = ImageTk.PhotoImage(Image.open("vacuum.jpg"))

    def moving_image(img_vacuum,x, y):
        for _ in range(grid_1_size):
            canvas.move(img_vacuum, x, y)
            time.sleep(0.01)
            master.update()


    def create_grid(canvas, x, y, size, grid_size):
        grid_1 = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                grid_1[i][j] = canvas.create_rectangle(x+j*grid_size,y+grid_size*i,
                x+grid_size+j*grid_size,y + grid_size+grid_size*i)
        return grid_1


    def dirt_tile(stack, x, y, size, grid_size):
            for i in range(len(stack)):
                if stack[i] == 1:
                    canvas.create_image(x+grid_size*(i%size)+image_size/2, y+grid_size*(i//size) +image_size/2, image = img_1)

    def motion(pos, img_vacuum, rectangle_x, rectangle_y):
            previous = pos[0]
            pos = pos[1:]
            for i in pos:
                if i - previous == 1:
                    moving_image(img_vacuum, 1, 0)
                    canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
                    previous = i
                elif i - previous == -1:
                    moving_image(img_vacuum, -1, 0)
                    canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
                    previous = i
                elif i - previous == size:
                    moving_image(img_vacuum, 0, 1)
                    canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
                    previous = i
                elif i - previous == -size:
                    moving_image(img_vacuum, 0, -1)
                    canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
                    previous = i
    def path_text(stack, canvas, x, y, text_add = ""):
        text ="  Path :"
        previous = stack[0]
        stack = stack[1:]
        for i in stack:
            if i - previous == 1:
                text = text + "R "
                # moving_image(img_vacuum, 1, 0)
                # canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
                previous = i
            elif i - previous == -1:
                text = text + "L "
                # moving_image(img_vacuum, -1, 0)
                # canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
                previous = i
            elif i - previous == size:
                text = text + "D "
                # moving_image(img_vacuum, 0, 1)
                # canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
                previous = i
            elif i - previous == -size:
                text = text + "U "
                # moving_image(img_vacuum, 0, -1)
                # canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
                previous = i
        text = text + text_add
        canvas.create_text(x, y, text= text, anchor = "nw")
    def nodes_text(stack, canvas, x, y, text_add = ""):
        text = "" +text_add
        text =text + str(stack[1]) + " nodes are generated"
        canvas.create_text(x, y, text= text, anchor = "nw")
    def node_mem_text(canvas, x, y, text_add = ""):
        text = "" +text_add
        text =text +" " + str(436)+" bytes" + " to max " + str(2*436)+" bytes"
        canvas.create_text(x, y, text= text, anchor = "nw")
    def aux_size_text(stack, canvas, x, y, text_add = ""):
        text = "" +text_add
        text =text +" " + str(stack[0]) + " is the auxilary size of stack/queue"
        canvas.create_text(x, y, text= text, anchor = "nw")
    def cost_text(stack, canvas, x, y, text_add = ""):
        text = "" +text_add
        text =text + "" + "Cost function " + str(len(stack)*2+vacuum.dirt*1)
        canvas.create_text(x, y, text= text, anchor = "nw")
    def time_text(stack, canvas, x, y, text_add = ""):
        text = "" +text_add
        text =text + "" + "Time taken " + str(stack[0])
        canvas.create_text(x, y, text= text, anchor = "nw")
    def total_mem_text(stack, canvas, x, y, text_add =""):
        text = "" + text_add
        text =text + "" + " total memory for ids is in the range of " +str(stack[0]*436)+" bytes " + " to " + str(stack[0]*2*436)+ " bytes"
        canvas.create_text(x, y, text= text, anchor = "nw")

    # def dirt_tile(master, x, y, size, grid_size):
    #     for i in range(len(stack[1])):
    #         if stack[1][i] == 1:
    #             canvas.create_image(x+grid_size*(i%size)+image_size/2, y+grid_size*(i//size) +image_size/2, image = img_1)
    if value == "display":
                grid_1 = create_grid(canvas, rectangle_1_x, rectangle_1_y, size, grid_1_size)
                # img_vacuum = canvas.create_image(rectangle_1_x+image_size/2, rectangle_1_y+image_size/2, image = img_2)
                dirt_tile(root_node.state, rectangle_1_x, rectangle_1_y, size, grid_1_size)
                # img_vacuum1 = canvas.create_image(rectangle_2_x+image_size/2, rectangle_2_y+image_size/2, image = img_3)
                grid_2 = create_grid(canvas, rectangle_2_x, rectangle_2_y, size, grid_2_size)
                dirt_tile(root_node.state, rectangle_2_x, rectangle_2_y, size, grid_1_size)
    elif value == "motion":
        stack = idfs.i_d_f_s(root_node)
        img_vacuum = canvas.create_image(rectangle_1_x+image_size/2, rectangle_1_y+image_size/2, image = img_2)
        # grid_1 = create_grid(canvas, rectangle_1_x, rectangle_1_y, size, grid_1_size)
        # dirt_tile(stack, rectangle_1_x, rectangle_1_y, size, grid_1_size)
        # img_vacuum = canvas.create_image(rectangle_1_x+image_size/2, rectangle_1_y+image_size/2, image = img_2)
        motion(stack[0], img_vacuum, rectangle_1_x, rectangle_1_y)
        canvas2.create_text(10, 10, text= "T1 IDS Analysis", anchor = "nw")
        path_text(stack[0], canvas2, 20, 30, "  IDFS")
        nodes_text(stack[2], canvas2, 20, 50, "R1: ")
        node_mem_text(canvas2, 20, 70, "R2: ")
        aux_size_text(stack[2], canvas2, 20, 90, "R3: ")
        cost_text(stack[0], canvas2, 20, 110, "R4: ")
        time_text(stack[3], canvas2, 20, 130, "R5: ")




        stack = bfs.b_f_s(root_node)
        img_vacuum1 = canvas.create_image(rectangle_2_x+image_size/2, rectangle_2_y+image_size/2, image = img_3)
        # grid_2 = create_grid(canvas, rectangle_2_x, rectangle_2_y, size, grid_2_size)
        # img_vacuum1 = canvas.create_image(rectangle_2_x+image_size/2, rectangle_2_y+image_size/2, image = img_3)
        # dirt_tile(stack, rectangle_2_x, rectangle_2_y, size, grid_1_size)
        motion(stack[0], img_vacuum1, rectangle_2_x, rectangle_2_y)
        canvas2.create_text(10, 170, text= "T2 BFS Analysis", anchor = "nw")
        path_text(stack[0], canvas2, 20, 190, "  BFS")
        nodes_text(stack[2], canvas2, 20, 210, "R6: ")
        node_mem_text(canvas2, 20, 230, "R7: ")
        aux_size_text(stack[2], canvas2, 20, 250, "R8: ")
        cost_text(stack[0], canvas2, 20, 270, "R9: ")
        time_text(stack[3], canvas2, 20, 290, "R10: ")
        # canvas2.create_text(10, 170, y, text= "R11: Average is nearly ", anchor = "nw")


    # canvas.pack()
    #
    # def dirt_tile(stack, x, y, size, grid_size):
    #     for i in range(len(stack[1])):
    #         if stack[1][i] == 1:
    #             canvas.create_image(x+grid_size*(i%size)+image_size/2, y+grid_size*(i//size) +image_size/2, image = img_1)
    #
    # def motion(pos, img_vacuum, rectangle_x, rectangle_y):
    #     previous = pos[0]
    #     pos = pos[1:]
    #     for i in pos:
    #         if i - previous == 1:
    #             moving_image(img_vacuum, 1, 0)
    #             canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
    #             previous = i
    #         elif i - previous == -1:
    #             moving_image(img_vacuum, -1, 0)
    #             canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
    #             previous = i
    #         elif i - previous == size:
    #             moving_image(img_vacuum, 0, 1)
    #             canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
    #             previous = i
    #         elif i - previous == -size:
    #             moving_image(img_vacuum, 0, -1)
    #             canvas.create_line(rectangle_x+(previous%size)*grid_1_size + grid_1_size/2, rectangle_y + (previous//size)*grid_1_size + grid_1_size/2, rectangle_x+(i%size)*grid_1_size+ grid_1_size/2, rectangle_y + (i//size)*grid_1_size +grid_1_size/2)
    #             previous = i

    # motion(stack[0], img_vacuum, rectangle_1_x, rectangle_1_y)
    master.mainloop()
    # tkinter.Tk().update()
# grid_1(master, canvas)
    # master.mainloop()


# class vacuum:
#         def __init__(self, x, y, g_size, img_size,canvas , file):
#                 self.x = x
#                 self.y = y
#                 self.g_size = g_size
#                 self.img_size = img_size
#                 self.canvas = canvas
#                 self.file = file

#                 self.img_open_vacuum = ImageTk.PhotoImage(Image.open(self.file))
#                 self.img_vacuum = self.canvas.create_image(self.x+self.img_size/2, self.y+self.img_size/2, image = self.img_open_vacuum)

#         def moving_image(self,x, y):
#                 for _ in range(self.g_size):
#                         self.canvas.move(self.img_vacuum, x, y)
#                         time.sleep(0.01)
#                         master.update()

#         def move_vacuum(self, action):
#                 if action =="right":
#                         self.moving_image(1, 0)
#                 elif action == "left":
#                         self.moving_image(-1, 0)
#                 elif action == "up":
#                         self.moving_image(0, -1)
#                 elif action == "down":
#                         self.moving_image(0, 1)


# def dirt_generator(p):
#     tile = [0]*100
#     num = random.sample(range(100), p)
#     for i in num:
#         tile[i] = 1
#     return tile




# def moving_image(img_vacuum, x):
#         canvas.move(img_vacuum, x, 0)
#         time.sleep(0.01)



# Image generator code


# vacuum_object = vacuum(rectangle_1_x, rectangle_1_y, grid_1_size, image_size, canvas, "dirt.jpg")

# tiles = dirt_generator(15)




# for i in range(10):
#     canvas.create_image(rectangle_1_x+image_size/2, rectangle_1_y+image_size/2+ i*grid_1_size, image = img_1)


# moving_image_y(img_vacuum,1)
# for _ in range(9):
#     moving_image_x(img_vacuum, -1)
# moving_image_y(img_vacuum,1)
# for _ in range(9):
#     moving_image_x(img_vacuum, 1)
# moving_image_y(img_vacuum,1)
# for _ in range(9):
#     moving_image_x(img_vacuum, -1)


# master.mainloop()
