# Importing Tkinter
import tkinter as tk
from tkinter import ttk
import sv_ttk
import customtkinter

# Importing classes
from classes.concessionario import Concessionario

# Importing components
from components.notebook import Notebook


class App(tk.Tk):
    def __init__(self) -> None:
        # Inizzializzazione della finestra root
        super().__init__()
        self.title("Gestione Veicoli")
        self.geometry("800x600")
        self.resizable(False, False)

        # Inizializzazione della concessionaria
        self.concessionaria = Concessionario(
            "Concessionaria",
            "Via Roma",
            "Roma",
            12345,
            "RM",
            "1234567890",
            "concessionaria@gmail.com",
        )

        # Renderizzazione dei componenti
        self.tabs = Notebook(self)


if __name__ == "__main__":
    app = App()
    sv_ttk.set_theme("dark")
    customtkinter.set_appearance_mode("dark")
    app.mainloop()
