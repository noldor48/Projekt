import tkinter as tk
from tkinter import messagebox
import re

def paarbaude_talrunis():
    talrunis = entryt.get()
    pattern = r'^[+]+[?=.*\d]{3,}$'
    
    if re.match(pattern, talrunis):
        messagebox.showinfo("Rezultāts", "Talrunis ir derīgs!")
    else:
        messagebox.showerror("Rezultāts", "Talrunis nav derīgs!")

root = tk.Tk()
root.title("Talrunja pārbaude")

tk.Label(root, text="Ievadiet talruni:").pack(pady=5)
entryt = tk.Entry(root, width=30)
entryt.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_talrunis).pack(pady=5)

root.mainloop()