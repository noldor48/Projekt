import tkinter as tk
from tkinter import messagebox
import re

def paarbauda_vardu():
    suns = entry_vards.get()
    pattern = r'^[A-ZĀ-Ž]+[a-zā-ž]*$|^[A-ZĀ-Ž][a-zā-ž]+\s[A-ZĀ-Ž][a-zā-ž]+$'
    if re.match(pattern, suns):
        messagebox.showinfo("Rezultāts", "Suņja dati ir derīgi!")
    else:
        messagebox.showerror("Rezultāts", "Suņja dati nav derīgi!")

def paarbauda_dati():
    suns = entry_date.get()
    pattern = r'[0-9]{2}+[.]+[0-9]{2}+[.]+[0-9]{4}+$|[0-9]{2}+[/]+[0-9]{2}+[/]+[0-9]{4}+$'
    if re.match(pattern, suns):
        messagebox.showinfo("Rezultāts", "Suņja dati ir derīgi!")
    else:
        messagebox.showerror("Rezultāts", "Suņja dati nav derīgi!")

def paarbauda_vietu():
    suns = entry_place.get()
    pattern = r'^[A-ZĀ-Ž]+[a-zā-ž]*$|^[A-ZĀ-Ž][a-zā-ž]+\s[a-zĀ-Ž][a-zā-ž]+$|^[A-ZĀ-Ž][a-zā-ž]+\s[a-zĀ-Ž][a-zā-ž][,]+\s^[A-ZĀ-Ž][a-zā-ž]+\s[a-zĀ-Ž][a-zā-ž]+$'
    if re.match(pattern, suns):
        messagebox.showinfo("Rezultāts", "Suņja dati ir derīgi!")
    else:
        messagebox.showerror("Rezultāts", "Suņja dati nav derīgi!")

root = tk.Tk()
root.title("Suņa dati")
root.geometry(f"300x300+{int((root.winfo_screenwidth())/2)-150}+{int((root.winfo_screenheight())/2)-150}")

tk.Label(root, text="Ievadiet suņja vārdu:").pack(pady=5)
entry_vards = tk.Entry(root, width=30)
entry_vards.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbauda_vardu).pack(pady=5)

tk.Label(root, text="Ievadiet suņja dzimšanas datumu:").pack(pady=5)
entry_date = tk.Entry(root, width=30)
entry_date.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbauda_dati).pack(pady=5)

tk.Label(root, text="Ievadiet suņja atrašanas vietu:").pack(pady=5)
entry_place = tk.Entry(root, width=30)
entry_place.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbauda_vietu).pack(pady=5)

root.mainloop()