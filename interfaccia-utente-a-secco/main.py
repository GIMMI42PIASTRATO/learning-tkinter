import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def show_message_send():
    messagebox.showinfo("Info", "Messaggio inviato con successo")


# Creare una nuova istanza dell'interfaccia grafica
root = tk.Tk()
root.title("LightMail")

# Creazione e visualizzazione dei frame
frame0 = tk.Frame(root)
frame1 = tk.Frame(root, border=5, relief="ridge")
frame2 = tk.Frame(root)
frame3 = tk.Frame(root, border=5, relief="ridge")
frame4 = tk.Frame(root)

frame0.grid(column=0, row=0, columnspan=2)
frame1.grid(column=0, row=1)
frame2.grid(column=1, row=1)
frame3.grid(column=0, row=2)
frame4.grid(column=1, row=2)

# Frame 0
# Combobox per selezionare la casella di posta
label0 = tk.Label(frame0, text="Casella di posta: ")
label0.grid(row=0, column=0)
selezionaCasella = ttk.Combobox(
    frame0,
    width=50,
    values=[
        "Tutte le cartelle",
        "Da leggere",
        "Posta in arrivo",
        "Posta inviata",
        "Posta eliminata",
    ],
)
selezionaCasella.current(0)
selezionaCasella.grid(row=1, column=0)

# Frame 1
# Creazione e visualizzazione dei label
label1 = tk.Label(frame1, text="Nuovo messaggio")
# columnspan=2: dice che questo widget deve occupare 2 colonne, visto che ci sono solo due colonne, occupa tutta la riga e si centra
label1.grid(row=0, column=0, columnspan=2)

# Label destinatario e entry destinatario
labelDestinatario = tk.Label(frame1, text="Destinatario: ")
labelDestinatario.grid(row=1, column=0)
destinatario = tk.Entry(frame1, width=50)
destinatario.grid(row=1, column=1)

# Label oggetto e entry oggetto
labelOggetto = tk.Label(frame1, text="Oggetto: ")
labelOggetto.grid(row=2, column=0)
oggetto = tk.Entry(frame1, width=50)
oggetto.grid(row=2, column=1)

# Checkbox modalità riservata
modalitaRiservata = tk.Checkbutton(frame1, text="Modalità riservata")
modalitaRiservata.grid(row=3, column=0)

# Creazione radiobutton cc e ccn
none = tk.Radiobutton(frame1, text="None", value="None")
none.grid(row=4, column=0)
cc = tk.Radiobutton(frame1, text="Cc", value="Cc")
cc.grid(row=4, column=1)
ccn = tk.Radiobutton(frame1, text="Ccn", value="Ccn")
ccn.grid(row=4, column=2)

# Creazione e visualizzazione del bottone
button1 = tk.Button(frame1, text="Invia", command=show_message_send)
button1.grid(row=5, columnspan=2)


# Frame 2
# testo email
label2 = tk.Label(frame2, text="Testo email")
label2.pack()

textArea = tk.Text(frame2, width=50, height=10)
textArea.pack()

# Frame 3
# Creazione e visualizzazione dei label e della listbox rubrica
labelRubrica = tk.Label(frame3, text="Rubrica")
labelRubrica.grid(row=0, column=0)
rubricaList = tk.Listbox(frame3, width=70, height=10)
rubricaList.insert(0, "Mario Rossi:     mario.rossi@gmail.com")
rubricaList.insert(1, "Luigi Verdi:     luigi.verdi@protonmail.com")
rubricaList.insert(2, "Giuseppe Bianchi:     giuseppe.bianchi@itispininfarina.it")
rubricaList.grid(row=1, column=0)

# Frame 4
# Filigrana
labelFiligrana = tk.Label(frame4, text="LightMail GNU/GPL v1.0")
labelFiligrana.pack()

# Inizializza il ciclo degli eventi
root.mainloop()
