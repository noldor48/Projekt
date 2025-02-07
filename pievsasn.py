import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Datubazes atvershana
conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

#Galvena funkcija
def pievienot_sasniegumu():
    def sasniegums_piev():
        date = datums_entry.get()
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
    ttk.Label(root, text="Cilveka ID:").pack()
    cilveka_id_entry = ttk.Entry(root)
    cilveka_id_entry.pack()

    ttk.Label(root, text="Datums:").pack()
    datums_entry = ttk.Entry(root)
    datums_entry.pack()

    ttk.Label(root, text="Vieta:").pack()
    vieta_entry = ttk.Entry(root)
    vieta_entry.pack()

    ttk.Label(root, text="Sasniegums:").pack()
    sasniegums_entry = ttk.Entry(root)
    sasniegums_entry.pack()

    saglabat_btn = ttk.Button(root, text="Saglabāt", command=sasniegums_piev)
    saglabat_btn.pack(pady=10)
