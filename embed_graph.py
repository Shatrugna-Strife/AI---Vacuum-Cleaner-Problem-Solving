import tkinter
from tkinter import *

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack(side = tkinter.RIGHT)
root.wm_title("Embedding in Tk")

frame1 = tkinter.Frame(root)
frame1.pack(side = tkinter.LEFT)
# layer = tkinter.Canvas(root,width= 1800,height= 800)
# tkinter.Label(frame1, text="Fuck oFF",).pack()
  
text = tkinter.Text(frame1)  
text.insert(tkinter.INSERT, "Name.....")  
text.insert(tkinter.INSERT, "Name.....") 
text.insert(tkinter.END, "Salary.....")  
text.pack()  

fig = Figure(figsize=(7, 7), dpi=100)
t = np.arange(0, 3, .01)
ax_1 = fig.add_subplot(221)
ax_1.plot(t, 2 * np.sin(2 * np.pi * t))
ax_2 = fig.add_subplot(222)
ax_2.plot(t, 2 * np.sin(2 * np.pi * t))
ax_3 = fig.add_subplot(223)
ax_3.plot(t, 2 * np.sin(2 * np.pi * t))
ax_4 = fig.add_subplot(224)
ax_4.plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=frame) 
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
# layer.pack()
toolbar = NavigationToolbar2Tk(canvas, frame)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)

# layer.mainloop()
tkinter.mainloop()
