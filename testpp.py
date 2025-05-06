from tkinter import *
import tkinter
root = Tk()

canvas = tkinter.Canvas(root, borderwidth=0, background="#000000")
frame= tkinter.Frame(canvas, background="#000000")

v = Scrollbar(frame)
v.pack(side = RIGHT, fill = Y)
t = Text(root, width = 15, height = 15, wrap = NONE, 
        yscrollcommand = v.set)

root.mainloop()
