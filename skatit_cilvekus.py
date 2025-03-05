import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from rediget_personu import rediget_cilveku
from dzest_cilveku import dzest_cilveku
from pievienot_sasniegumu import pievienot_sasniegumu
from jauna_cv import cv_izveidoshana

#Datubazes atvershana
conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

#Galvena funkcija
def skatit_cilvekus():
    def opa():
        cursor.execute("SELECT * FROM Personas")
        rezultati = cursor.fetchall()
        if rezultati:
            rezultati_str = ""
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
                cv_pievien = ttk.Button(root, text="Izveidot cv", command=cv_izveidoshana)
                cv_pievien.pack(pady=10)
                ttk.Label(root, text="-----------------------------------------------------------", background="#000000", foreground="white").pack()
        else:
            messagebox.showinfo("Rezultāti", "Netika atrasts neviens cilveks.")

    # Loga veidoshana
    root = Tk()
    root.title("Cilveki")
    root.iconbitmap(default="useri.ico")
    root.geometry(f"300x600+{int((root.winfo_screenwidth())/2)-150}+{int((root.winfo_screenheight())/2)-300}")
    root.configure(bg='#000000')

    opa()