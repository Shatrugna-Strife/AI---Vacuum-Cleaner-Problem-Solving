import tkinter
from tkinter import *
import gui
import vacuum
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import os
import sys
# tile_size = 6
# vacuum.side = 4

root_node = vacuum.create_root_node(vacuum.dirt)
root = tkinter.Tk()
root.geometry("1800x750")
frame = tkinter.Frame(root)
frame.pack(side = tkinter.RIGHT)
frame1 = tkinter.Frame(root)
frame1.pack(side = tkinter.TOP)
frame2 = tkinter.Frame(root)
frame2.pack(side = tkinter.LEFT)

root.wm_title("YEah")
msg = "\nClick the First Button to display the environment.Press second button to show the path taken by vacuum cleaner(press the first button then press this)\nThe left grid is of the result from IDS(Iterative Deepening Search) and right grid is of BFS(Breadth First Search)\nOn clicking reenter, if error appears enter some random value and click reenter button once again\n"
message = tkinter.Message(frame2, text = msg)
canvas1 = tkinter.Canvas(frame2, width = 600, height = 700 , bg = "yellow")
# canvas1.place(x = 0, y = 0)
# canvas1.pack(side = tkinter.BOTTOM)
# message = tkinter.Message(frame2, text = "hello")
message.pack(side = tkinter.TOP)
canvas1.pack(side = tkinter.BOTTOM)
canvas2 = tkinter.Canvas(frame, width = 1100, height = 500, bg = "pink")
# canvas2.place(x = 0, y = 0)
canvas2.pack(side = tkinter.TOP)
# layer = tkinter.Canvas(root, width = 1000, height = 700)
def print_me():
    # canvas2.pack_forget()
    gui.grid_1(root, canvas2, canvas1, root_node, "display")
    # canvas2.pack(side = tkinter.TOP, bg = "white")
def print_me1():
    # canvas2.create_text(40, 40, text = "Fuck oof")
    # gui.grid_1(root, canvas2, root_node, "display")
    gui.grid_1(root, canvas2, canvas1, root_node, "motion")
    # canvas2.create_text(20, 10, text = "Fuck off" )
def print_me2():
    root.destroy()
    # os.execv("embed_graph.py")
    os.execv(sys.executable, ['python'] + sys.argv)
    # os.execv(sys.executable, ['python'])
    # python = sys.executable
    # os.execl(python, python, * sys.argv)
def print_me3():
    # pass
    canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas1.create_text(10, 350,text = "G3: Blue for IDFS and Red for BFS\nG4: IDFS Analysis for 5x5 tiles" , anchor= "nw")


button1 = tkinter.Button(frame1, text = "Display Environment", command = print_me)
button1.pack(side = tkinter.LEFT)
button2 = tkinter.Button(frame1, text = "Path Diaplay", command = print_me1)
button2.pack(side = tkinter.LEFT)
button3 = tkinter.Button(frame1, text = "Reenter tile and dirt values", command = print_me2)
button3.pack(side = tkinter.LEFT)
button4 = tkinter.Button(frame1, text = "Graph", command = print_me3)
button4.pack(side = tkinter.LEFT)

# layer = tkinter.Canvas(root,width= 1800,height= 800)
# tkinter.Label(frame1, text="Fuck oFF",).pack()

# text = tkinter.Text(frame1)
# text.insert(tkinter.INSERT, "Name.....")
# text.insert(tkinter.INSERT, "Name.....")
# text.insert(tkinter.END, "Salary.....")
# text.pack()
# layer.create_text(0,100,text = "fUcK oFF")

# layer.pack()
fig = Figure(figsize=(5, 2), dpi=100)
# t = np.arange(0, 3, .01)
test1_tile = [3, 4, 5, 6, 7, 8, 9]
test1_idfs = [0.0009953975677490234, 0.0009975433349609375, 0.016935110092163086, 0.05388212203979492, 2.1661813259124756, 12.364975452423096, 88.44031715393066]
test1_bfs = [0.0004992485046386719, 0.0011005401611328125, 0.0019888877868652344, 0.007222890853881836, 0.2633225917816162, 3.516629457473755, 96.26532435417175]
test2_x = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
test2_idfs = [0.009003639221191406, 0.048897743225097656, 0.6193442344665527, 0.7240993976593018, 2.4797027111053467, 0.8078408241271973, 9.052439212799072, 5.181188106536865, 16.278591871261597, 7.121971607208252, 8.055477857589722, 22.96227765083313, 23.20203733444214, 13.948385238647461, 39.88882780075073, 22.129606008529663, 39.635128021240234, 50.81204700469971, 44.73095703125, 50.40432024002075]
ax_1 = fig.add_subplot(121)
ax_1.plot(test1_tile, test1_bfs)
ax_1.plot(test1_tile, test1_idfs)
# ax_1.plot(t, 2 * np.sin(2 * np.pi * t))
ax_2 = fig.add_subplot(122)
ax_2.plot(test2_x, test2_idfs)
# ax_2.plot(t, 2 * np.sin(2 * np.pi * t))
# ax_3 = fig.add_subplot(123)
# ax_3.plot(t, 2 * np.sin(2 * np.pi * t))
# ax_4 = fig.add_subplot(124)
# ax_4.plot(t, 2 * np.sin(2 * np.pi * t))
# label1 = tkinter.Label(frame1, text = "hello")
# label1.place(x = 0, y = 0)
# label1.pack()
canvas = FigureCanvasTkAgg(fig, master=frame)
# canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()


# canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)
# canvas.get_tk_widget().pack(side=, fill=tkinter.BOTH, expand=1)
# toolbar = NavigationToolbar2Tk(canvas, frame)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)

# layer.mainloop()
tkinter.mainloop()
