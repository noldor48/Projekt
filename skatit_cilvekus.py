import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from rediget import rediget_cilveku
from drest import dzest_cilveku
from pievsasn import pievienot_sasniegumu

conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

def skatit_cilvekus():
    def opa():
        cursor.execute("SELECT * FROM Personas")
        rezultati = cursor.fetchall()
        if rezultati:
            rezultati_str = ""
            scroll_bar = Scrollbar(root) 
            scroll_bar.pack( side = RIGHT, fill = Y )
            ttk.Label(root, text="-----------------------------------------------------------", background="#000000", foreground="white").pack()
            for r in rezultati:
                rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}, {r[5]}, {r[6]}\n"
                ttk.Label(root, text=f"Atrasts ID:{r[0]}\nVards uzvards: {r[1]} {r[2]}\nDzimsanas datums: {r[3]}\nvecums: {r[4]}\ndzimums: {r[5]}\nemail: {r[6]}", width=50).pack()
                meklēt_btn = ttk.Button(root, text="Redigiet", command=rediget_cilveku)
                meklēt_btn.pack(pady=10)
                dzest_btn = ttk.Button(root, text="Dzest", command=dzest_cilveku)
                dzest_btn.pack(pady=10)
                sas_pievien = ttk.Button(root, text="Pievienot sasniegumu", command=pievienot_sasniegumu)
                sas_pievien.pack(pady=10)
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