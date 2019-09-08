import tkinter
import random
from PIL import ImageTk, Image
import time
grid_1_size = 50
rectangle_1_x = 10
rectangle_1_y = 10

image_size = 50
vacuum_pos_x = image_size/2
vacuum_pos_y = image_size/2
size = 10

grid_2_size = 50
rectangle_2_x = rectangle_1_x + size*grid_1_size + grid_2_size
rectangle_2_y = rectangle_1_y

master = tkinter.Tk()
canvas = tkinter.Canvas(master, width = 1500, height = 800)

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


def dirt_generator(p):
    tile = [0]*100
    num = random.sample(range(100), p)
    for i in num:
        tile[i] = 1
    return tile

def create_grid(master, x, y, size, grid_size):
    grid_1 = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            grid_1[i][j] = canvas.create_rectangle(x+j*grid_size,y+grid_size*i,
            x+grid_size+j*grid_size,y + grid_size+grid_size*i)
    return grid_1


# def moving_image(img_vacuum, x):
#         canvas.move(img_vacuum, x, 0)
#         time.sleep(0.01)

def moving_image(img_vacuum,x, y):
    for _ in range(grid_1_size):
        canvas.move(img_vacuum, x, y)
        time.sleep(0.01)
        master.update()

# Image generator code
img_1 = ImageTk.PhotoImage(Image.open("dirt.jpg"))

# vacuum_object = vacuum(rectangle_1_x, rectangle_1_y, grid_1_size, image_size, canvas, "dirt.jpg")

# tiles = dirt_generator(15)
# for i in range(100):
#     if tiles[i] == 1:
#         canvas.create_image(rectangle_1_x+grid_1_size*(i%10)+image_size/2, rectangle_1_y+grid_1_size*(i//10) +image_size/2, image = img_1)



# for i in range(10):
#     canvas.create_image(rectangle_1_x+image_size/2, rectangle_1_y+image_size/2+ i*grid_1_size, image = img_1)
img_2 = ImageTk.PhotoImage(Image.open("vacuum.jpg"))
img_vacuum = canvas.create_image(rectangle_1_x+grid_1_size+image_size/2, rectangle_1_y+image_size/2, image = img_2)




grid_1 = create_grid(master, rectangle_1_x, rectangle_1_y, size, grid_1_size)
grid_2 = create_grid(master, rectangle_2_x, rectangle_2_y, size, grid_2_size)
canvas.pack()

# for _ in range(8):
#     moving_image_x(img_vacuum, 1)
# moving_image_y(img_vacuum,1)
# for _ in range(9):
#     moving_image_x(img_vacuum, -1)
# moving_image_y(img_vacuum,1)
# for _ in range(9):
#     moving_image_x(img_vacuum, 1)
# moving_image_y(img_vacuum,1)
# for _ in range(9):
#     moving_image_x(img_vacuum, -1)


master.mainloop()
