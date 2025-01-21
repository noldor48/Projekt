import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

def pievienot_cilveku():
    def saglabat_cilveku():
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        birthday = birthday_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        email = email_entry.get()

        if firstname and lastname and birthday.isdigit():
            cursor.execute('''INSERT INTO Personas (firstname, lastname, birthday, age, gender, email)VALUES (?, ?, ?, ?, ?, ?)''', (firstname, lastname, birthday, age, gender, email))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Cilveks pievienots!")
            root.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")


    root = Tk()
    root.title("Cilveku pievienoshana")
    root.iconbitmap(default="useri.ico")
    root.geometry(f"300x450+{int((root.winfo_screenwidth())/2)-150}+{int((root.winfo_screenheight())/2)-225}")
    root.configure(bg='#000000')

    ttk.Label(root, text="Vārds:").pack()
    firstname_entry = ttk.Entry(root)
    firstname_entry.pack()

    ttk.Label(root, text="Uzvārds:").pack()
    lastname_entry = ttk.Entry(root)
    lastname_entry.pack()

    ttk.Label(root, text="Dzimšanas gads:").pack()
    birthday_entry = ttk.Entry(root)
    birthday_entry.pack()

    ttk.Label(root, text="Vecums:").pack()
    age_entry = ttk.Entry(root)
    age_entry.pack()

    ttk.Label(root, text="Dzimums:").pack()
    gender_entry = ttk.Entry(root)
    gender_entry.pack()

    ttk.Label(root, text="email:").pack()
    email_entry = ttk.Entry(root)
    email_entry.pack()

    saglabat_btn = ttk.Button(root, text="Saglabāt", command=saglabat_cilveku)
    saglabat_btn.pack(pady=10)