import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import re

#Datubazes atvershana
conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

#Galvena funkcija
def rediget_cilveku():
    def calendar_view():
        def print_sel():
            print(cal.selection_get())
            global atime
            atime = cal.selection_get()
            top.destroy()
        top = tk.Toplevel(root)
        cal = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1", year=2025, month=2, day=5)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()

    def saglabat_cilveku():
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        birthday = atime
        atime1 = str(atime)
        age = int(datetime.now().year) - int(atime1[0:4])
        gender = gender_entry.get()
        email = email_entry.get()
        personid = id_entry.get()

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
        if re.match(pattern, email):
            if firstname and lastname and birthday: 
                cursor.execute('''UPDATE Personas SET firstname = ?, lastname = ?, birthday = ?, age = ?, gender = ?, email = ? where person_id = ?''', (firstname, lastname, birthday, age, gender, email, personid))
                conn.commit()
                messagebox.showinfo("Veiksmīgi", "Cilveks redigets!")
                root.destroy()
            else:
                messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")
        else:
            messagebox.showerror("Rezultāts", "E-pasta adrese nav derīga!")

    # Loga veidoshana
    root = Tk()
    root.title("Cilveku redigeshana")
    root.iconbitmap(default="useri.ico")
    root.geometry(f"300x450+{int((root.winfo_screenwidth())/2)-150}+{int((root.winfo_screenheight())/2)-225}")
    root.configure(bg='#000000')

    #Datus ievadishanas pieprasijums
    ttk.Label(root, text="ID:", background="gold").pack()
    id_entry = ttk.Entry(root)
    id_entry.pack()

    ttk.Label(root, text="Vārds:", background="gold").pack()
    firstname_entry = ttk.Entry(root)
    firstname_entry.pack()

    ttk.Label(root, text="Uzvārds:", background="gold").pack()
    lastname_entry = ttk.Entry(root)
    lastname_entry.pack()

    ttk.Label(root, text="Dzimšanas datums:", background="gold").pack()
    birthday_entry = ttk.Button(root, text='Atvert kalendari', command= calendar_view).pack(padx=10, pady=10)

    ttk.Label(root, text="Dzimums:", background="gold").pack()
    dzimums = ["Vīrietis", "Sieviete"]
    gender_entry = ttk.Combobox(root,values=dzimums)
    gender_entry.pack(padx=10, pady=10)

    ttk.Label(root, text="email:", background="gold").pack()
    email_entry = ttk.Entry(root)
    email_entry.pack()

    saglabat_btn = ttk.Button(root, text="Saglabāt", command=saglabat_cilveku)
    saglabat_btn.pack(pady=10)