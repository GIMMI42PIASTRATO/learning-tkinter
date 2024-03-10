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
    def __init__(self, container, app):
        super().__init__(container)
        self.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(1, weight=2)

        self.concessionaria = app.concessionaria

        self.create_widgets()
        self.create_veicoli_widgets()

    def create_widgets(self):
        # Number of vehicles
        self.numero_veicoli_text = tk.StringVar()
        self.numero_veicoli = ttk.Label(
            self, textvariable=self.numero_veicoli_text, 
        )
        self.update_numero_veicoli()
        
         # Option Menu
        self.option_label = ttk.Label(self, text="Seleziona il tipo di veicolo: ")
        self.option_menu = OptionMenu(
            container=self,
            options=["Tutti", "Autoveicoli", "Autocarri", "Motoveicoli"],
            concessionaria=self.concessionaria,
        )

        # Place the widgets
        self.numero_veicoli.grid(row=0, column=0, sticky="w", padx=(10, 0))
        self.option_label.grid(row=0, column=1, sticky="e")

    def update_numero_veicoli(self):
        self.numero_veicoli_text.set(
            f"Numero di veicoli: {self.concessionaria.get_conteggio_veicoli()}"
        )

    def create_veicoli_widgets(self):
        # Clear the frame
        for widget in self.winfo_children():
            if widget != self.numero_veicoli and widget != self.option_label and widget != self.option_menu:
                widget.destroy()

        # Create the widgets
        for veicolo in self.concessionaria.get_veicoli_filtrati():
            pass
