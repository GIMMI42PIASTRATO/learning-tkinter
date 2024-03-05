# Importing Tkinter
import tkinter as tk
from tkinter import ttk

# Importing classes
from classes.autocarro import Autocarro
from classes.autoveicolo import Autoveicolo
from classes.motoveicolo import Motoveicolo

# Importing components
from components.notebook import Notebook


class App(tk.Tk):
    def __init__(self) -> None:
        # Inizzializzazione della finestra root
        super().__init__()
        self.title("Gestione Veicoli")
        self.geometry("800x600")
        self.resizable(False, False)

        # Renderizzazione dei componenti
        self.tabs = Notebook(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
