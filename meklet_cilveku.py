import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from rediget_personu import rediget_cilveku
#from dzest_cilveku import dzest_cilveku
from pievienot_sasniegumu import pievienot_sasniegumu
from jauna_cv import cv_izveidoshana

#Datubazes atvershana
conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

#Galvena funkcija
def meklet_cilveku():
    def sameklet_cilveku():
        vards = firstname_entry.get()
        if vards:
            cursor.execute("SELECT * FROM Personas WHERE firstname LIKE ?", (f"%{vards}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    #Funkcija kas dzest cilveku
                    def dzest_cilveku():  
                        def dzessana_cilveku():
                            personid = r[0]
                            if personid:
                                cursor.execute(f"DELETE FROM Personas WHERE person_id = {personid}")
                                conn.commit()
                                messagebox.showinfo("Veiksmīgi", "Cilveks dzests!")
                            else:
                                messagebox.showerror("Kļūda", "Nebija dziests!")

                        res=messagebox.askquestion('Dzēst cilveku', 'Vai tiešām vēlaties viņju dzēst?')
                        if res == 'yes' :
                            dzessana_cilveku()

                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}, {r[5]}, {r[6]}\n"
                    ttk.Label(root, text=f"Atrasts ID:{r[0]}\nVards uzvards: {r[1]} {r[2]}\nDzimsanas datums: {r[3]}\nvecums: {r[4]}\ndzimums: {r[5]}\nemail: {r[6]}", width=50, background="gold").pack()
                    meklēt_btn = ttk.Button(root, text="Redigiet", command=rediget_cilveku)
                    meklēt_btn.pack(pady=10)
                    dzest_btn = ttk.Button(root, text="Dzēst", command=dzest_cilveku)
                    dzest_btn.pack(pady=10)
                    sas_pievien = ttk.Button(root, text="Pievienot sasniegumu", command=pievienot_sasniegumu)
                    sas_pievien.pack(pady=10)
                    cv_pievien = ttk.Button(root, text="Izveidot cv", command=cv_izveidoshana)
                    cv_pievien.pack(pady=10)
                    ttk.Label(root, text="-----------------------------------------------------------", background="#000000", foreground="white").pack()
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens cilveks.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet vārdu!")


    # Loga veidoshana
    root = Tk()
    root.title("Cilveku mekleshana")
    root.iconbitmap(default="useri.ico")
    root.geometry(f"300x500+{int((root.winfo_screenwidth())/2)-150}+{int((root.winfo_screenheight())/2)-250}")
    root.configure(bg='#000000')

    #Datus ievadishanas pieprasijums
    ttk.Label(root, text="Cilveka vārds:", background="gold").pack()
    firstname_entry = ttk.Entry(root)
    firstname_entry.pack()

    meklēt_btn = ttk.Button(root, text="Meklēt", command=sameklet_cilveku)
    meklēt_btn.pack(pady=10)