from tkinter import *
from tkinter import ttk
from pievienot_cilveku import pievienot_cilveku
from meklet_cilveku import meklet_cilveku
from skatit_cilvekus import skatit_cilvekus

# Loga veidoshana
root1 = Tk()
root1.title("Project")
root1.iconbitmap(default="useri.ico")
root1.geometry(f"300x150+{int((root1.winfo_screenwidth())/2)-150}+{int((root1.winfo_screenheight())/2)-75}")
root1.configure(bg='#000000')

#Pogas
btn1 = ttk.Button(text="Pievienot cilveku", command=pievienot_cilveku, width=40)
btn1.place(relx = 0.5 , rely = 0.2, anchor = CENTER)

btn2 = ttk.Button(text="Meklet cilveku", command=meklet_cilveku, width=40)
btn2.place(relx = 0.5 , rely = 0.4, anchor = CENTER)

btn3 = ttk.Button(text="Skatit cilvekus", command=skatit_cilvekus, width=40)
btn3.place(relx = 0.5 , rely = 0.6, anchor = CENTER)

btn4 = ttk.Button(text="Iziet", command=exit, width=40)
btn4.place(relx = 0.5 , rely = 0.8, anchor = CENTER)

root1.mainloop()