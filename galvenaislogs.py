#import sqlite3
from tkinter import *
from tkinter import ttk
from pievienot_cilveku import pievienot_cilveku
from meklet_cilveku import meklet_cilveku
from skatit_cilvekus import skatit_cilvekus


#win= Tk()
#win.geometry("650x250")
#screen_width = win.winfo_screenwidth()
#screen_height = win.winfo_screenheight()
#screen_width1 = int(screen_width/2-150)
#screen_height1 = int(screen_height/2-300)



root = Tk()
root.title("Project")
root.iconbitmap(default="useri.ico")
root.geometry(f"300x150+{int((root.winfo_screenwidth())/2)-150}+{int((root.winfo_screenheight())/2)-75}")
root.configure(bg='#000000')

btn1 = ttk.Button(text="Pievienot cilveku", command=pievienot_cilveku)
btn1.pack(anchor="center", padx=6, pady=6)

btn2 = ttk.Button(text="Meklet cilveku", command=meklet_cilveku)
btn2.pack(anchor="center", padx=6, pady=6)

btn3 = ttk.Button(text="Skatit cilvekus", command=skatit_cilvekus)
btn3.pack(anchor="center", padx=6, pady=6)

root.mainloop()
