import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Datubazes atvershana
conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

#Galvena funkcija
def dzest_cilveku():  
    def dzessana_cilveku():
        personid = id_entry.get()
        if personid:
            cursor.execute(f"DELETE FROM Personas WHERE person_id = {personid}")
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Cilveks dzests!")
            root.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    #res=messagebox.askquestion('Dzest cilveku', 'Jus patiesam gribat vinju izdzest?')
    #if res == 'yes' :
    #    dzessana_cilveku()

    # Loga veidoshana
    root = Tk()
    root.title("Cilveku dzesšana")
    root.iconbitmap(default="useri.ico")
    root.geometry(f"300x150+{int((root.winfo_screenwidth())/2)-150}+{int((root.winfo_screenheight())/2)-75}")
    root.configure(bg='#000000')

    #Datus ievadishanas pieprasijums
    ttk.Label(root, text="ID:", background="gold").pack()
    id_entry = ttk.Entry(root)
    id_entry.pack()

    saglabat_btn = ttk.Button(root, text="Dzest", command=dzessana_cilveku)
    saglabat_btn.pack(pady=10)