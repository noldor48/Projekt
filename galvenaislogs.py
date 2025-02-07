from tkinter import *
from tkinter import ttk
from pievienot_cilveku import pievienot_cilveku
from meklet_cilveku import meklet_cilveku
from skatit_cilvekus import skatit_cilvekus

# Loga veidoshana
root = Tk()
root.title("Project")
root.iconbitmap(default="useri.ico")
root.geometry(f"300x150+{int((root.winfo_screenwidth())/2)-150}+{int((root.winfo_screenheight())/2)-75}")
root.configure(bg='#000000')

#Pogas
btn1 = ttk.Button(text="Pievienot cilveku", command=pievienot_cilveku)
btn1.pack(anchor="center", padx=6, pady=6)

btn2 = ttk.Button(text="Meklet cilveku", command=meklet_cilveku)
btn2.pack(anchor="center", padx=6, pady=6)

btn3 = ttk.Button(text="Skatit cilvekus", command=skatit_cilvekus)
btn3.pack(anchor="center", padx=6, pady=6)

btn3 = ttk.Button(text="Iziet", command=exit)
btn3.pack(anchor="center", padx=6, pady=6)

root.mainloop()
