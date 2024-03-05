import tkinter as tk
from tkinter import ttk
import os
import sys

# Adding the path to the sys.path
current_dir = os.path.dirname(__file__)
gestione_veicoli_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(gestione_veicoli_dir)

# Importing components
from components.option_menu import OptionMenu


class TabVeicoli(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(1, weight=2)

        self.create_widgets()

    def create_widgets(self):
        # Create the widgets
        self.numero_veicoli = ttk.Label(self, text="Numero veicoli: ")
        self.option_label = ttk.Label(self, text="Seleziona il tipo di veicolo: ")
        self.option_menu = OptionMenu(
            self, ["Tutto", "Autoveicoli", "Autocarri", "Motoveicoli"]
        )

        # Place the widgets
        self.numero_veicoli.grid(row=0, column=0, sticky="w", padx=(10, 0))
        self.option_label.grid(row=0, column=1, sticky="e")
