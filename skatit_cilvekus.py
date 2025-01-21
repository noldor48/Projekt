import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

def skatit_cilvekus():
    def opa():
        cursor.execute("SELECT * FROM Personas")
        rezultati = cursor.fetchall()
        ttk.Label(root, text="-----------------------------------------------------------", background="#000000", foreground="white").pack()
        if rezultati:
            rezultati_str = ""
            for r in rezultati:
                rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}, {r[5]}, {r[6]}\n"
                ttk.Label(root, text=f"Atrasts ID:{r[0]}\nVards uzvards: {r[1]} {r[2]}\nDzimsanas datums: {r[3]}\nvecums: {r[4]}\ndzimums: {r[5]}\nemail: {r[6]}", width=50).pack()
                ttk.Label(root, text="-----------------------------------------------------------", background="#000000", foreground="white").pack()
                #messagebox.showinfo("Rezultats",f"Atrasts ID:{r[0]}: {r[1]} {r[2]}, {r[3]}, vecums: {r[4]}, dzimums: {r[5]}\n")
        else:
            messagebox.showinfo("Rezultāti", "Netika atrasts neviens cilveks.")

    root = Tk()
    root.title("Cilveki")
    root.iconbitmap(default="useri.ico")
    root.geometry(f"300x600+{int((root.winfo_screenwidth())/2)-150}+{int((root.winfo_screenheight())/2)-300}")
    root.configure(bg='#000000')

    opa()