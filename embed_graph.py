import tkinter
from tkinter import *


from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.geometry("1400x700")
frame = tkinter.Frame(root)
frame.pack(side = tkinter.RIGHT)
frame1 = tkinter.Frame(root)
frame1.pack(side = tkinter.TOP)
frame2 = tkinter.Frame(root)
frame2.pack(side = tkinter.LEFT)

root.wm_title("YEah")
canvas1 = tkinter.Canvas(frame2, width = 600, height = 700 , bg = "red")
# canvas1.place(x = 0, y = 0)
canvas1.pack(side = tkinter.BOTTOM)
canvas2 = tkinter.Canvas(frame, width = 800, height = 500 , bg = "red")
# canvas2.place(x = 0, y = 0)
canvas2.pack(side = tkinter.TOP)
# layer = tkinter.Canvas(root, width = 1000, height = 700)
def print_me():
    canvas2.create_text(20, 10, text = "Fuck off" )
button1 = tkinter.Button(frame1, text = "click me", command = print_me)
button1.pack(side = tkinter.LEFT)



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
t = np.arange(0, 3, .01)
ax_1 = fig.add_subplot(121)
ax_1.plot(t, 2 * np.sin(2 * np.pi * t))
ax_2 = fig.add_subplot(122)
ax_2.plot(t, 2 * np.sin(2 * np.pi * t))
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
canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)
# canvas.get_tk_widget().pack(side="se", fill=tkinter.BOTH, expand=1)
# toolbar = NavigationToolbar2Tk(canvas, frame)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)

# layer.mainloop()
tkinter.mainloop()
