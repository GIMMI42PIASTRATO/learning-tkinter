import tkinter as tk
from tkinter import ttk


class TabAggiungiVeicolo(ttk.Frame):
    def __init__(self, container, app):
        super().__init__(container)
        self.grid(row=0, column=0, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        # Create the widgets
        self.label = ttk.Label(self, text="Aggiungi Veicolo")

        # Place the widgets
        self.label.grid(row=0, column=0)
