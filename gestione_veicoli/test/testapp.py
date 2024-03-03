# Importing Tkinter
import tkinter as tk
from tkinter import ttk

# Importing classes
from classes.autocarro import Autocarro
from classes.autoveicolo import Autoveicolo
from classes.motoveicolo import Motoveicolo


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Concessionario")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Create a notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create a frame
        self.frame = tk.Frame(self.notebook)
        self.notebook.add(self.frame, text="Veicoli")

        # Create a label
        self.label = tk.Label(self.frame, text="Veicoli")
        self.label.pack()

        # Create a button
        self.button = tk.Button(self.frame, text="Aggiungi veicolo")
        self.button.pack()

        # Create a listbox
        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack()

        # Create a frame
        self.frame2 = tk.Frame(self.notebook)
        self.notebook.add(self.frame2, text="Concessionario")

        # Create a label
        self.label2 = tk.Label(self.frame2, text="Concessionario")
        self.label2.pack()

        # Create a button
        self.button2 = tk.Button(self.frame2, text="Aggiungi concessionario")
        self.button2.pack()

        # Create a listbox
        self.listbox2 = tk.Listbox(self.frame2)
        self.listbox2.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
