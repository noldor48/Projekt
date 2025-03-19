import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar

#Datubazes atvershana
conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

#Galvena funkcija
def pievienot_sasniegumu():
    def calendar_view():
        def print_sel():
            print(cal.selection_get())
            global atime
            atime = cal.selection_get()
        top = tk.Toplevel(root)
        cal = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1", year=2025, month=2, day=5)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()
    def sasniegums_piev():
        date = atime
        vieta = vieta_entry.get()
        sasniegums = sasniegums_entry.get()
        perspecid = cilveka_id_entry.get()

        if perspecid and sasniegums:
            cursor.execute('''INSERT INTO Sasniegumi (datums, vieta, sasniegums, person_id)VALUES (?, ?, ?, ?)''', (date, vieta, sasniegums, perspecid))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Sasniegums pievienots!")
            root.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    # Loga veidoshana
    root = Tk()
    root.title("Sasnieguma pievienoshana")
    root.iconbitmap(default="useri.ico")
    root.geometry(f"400x600+{int((root.winfo_screenwidth())/2)-200}+{int((root.winfo_screenheight())/2)-300}")
    root.configure(bg='#000000') 

    #Datus ievadishanas pieprasijums
    ttk.Label(root, text="Cilveka ID:", background="gold").pack()
    cilveka_id_entry = ttk.Entry(root)
    cilveka_id_entry.pack()

    ttk.Label(root, text="Datums:", background="gold").pack()
    birthday_entry = ttk.Button(root, text='Atvert kalendari', command= calendar_view).pack(padx=10, pady=10)

    ttk.Label(root, text="Vieta:", background="gold").pack()
    vieta_entry = ttk.Entry(root)
    vieta_entry.pack()

    ttk.Label(root, text="Sasniegums:", background="gold").pack()
    sasniegums_entry = ttk.Entry(root)
    sasniegums_entry.pack()

    saglabat_btn = ttk.Button(root, text="Saglabāt", command=sasniegums_piev)
    saglabat_btn.pack(pady=10)
