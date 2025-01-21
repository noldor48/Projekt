from tkinter import *

def monitorwh():
    win= Tk()
    win.geometry("650x250")
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    screen_width1 = int(screen_width/2)
    screen_height1 = int(screen_height/2)

    print("Screen width:", screen_width1)
    print("Screen height:", screen_height1)
    win.destroy()
    return screen_height1, screen_width1

