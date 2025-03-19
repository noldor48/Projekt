import tkinter as tk
from tkinter import messagebox
import re

def paarbaude_email():
    email = entry.get()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        messagebox.showinfo("Rezultāts", "E-pasta adrese ir derīga!")
    else:
        messagebox.showerror("Rezultāts", "E-pasta adrese nav derīga!")

root = tk.Tk()
root.title("E-pasta pārbaude")

tk.Label(root, text="Ievadiet e-pasta adresi:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_email).pack(pady=5)

root.mainloop()