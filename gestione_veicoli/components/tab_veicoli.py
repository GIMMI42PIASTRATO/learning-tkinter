import tkinter as tk
from tkinter import ttk
from customtkinter import CTkScrollableFrame
import os
import sys

# Adding the path to the sys.path
current_dir = os.path.dirname(__file__)
gestione_veicoli_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(gestione_veicoli_dir)

# Importing components
from components.option_menu import OptionMenu
from components.veicolo_card import Card


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
            self,
            textvariable=self.numero_veicoli_text,
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
            if (
                widget != self.numero_veicoli
                and widget != self.option_label
                and widget != self.option_menu
            ):
                widget.destroy()

        # Card container
        self.card_container = CTkScrollableFrame(
            self, orientation="vertical", corner_radius=0, fg_color="#1c1c1c"
        )
        self.card_container.grid(
            row=1, column=0, columnspan=3, sticky="nsew", pady=(10, 0)
        )

        # Configure the grid
        self.grid_rowconfigure(1, weight=1)  # Espansione verticale
        self.grid_columnconfigure(0, weight=1)  # Espansione orizzontale

        # Define numers of columns
        num_columns = 3

        for i, veicolo in enumerate(self.concessionaria.get_veicoli_filtrati()):
            # Calculate column and row index
            row = i // num_columns
            column = i % num_columns
            # Create the card
            Card(self.card_container, veicolo, row=row, column=column)
