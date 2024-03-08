# Library Imports
import tkinter as tk
from tkinter import ttk
import sys
import os

# # Adding the path to the sys.path
# current_dir = os.path.dirname(__file__)
# gestione_veicoli_dir = os.path.abspath(os.path.join(current_dir, ".."))
# sys.path.append(gestione_veicoli_dir)

# Component Imports
from components.tab_veicoli import TabVeicoli
from components.tab_aggiungi_veicolo import TabAggiungiVeicolo


class Notebook(ttk.Notebook):
    def __init__(self, container) -> None:

        super().__init__(container)
        self.pack(fill="both", expand=True)

        tab_veicoli = TabVeicoli(self, app=container)
        self.add(tab_veicoli, text="Veicoli")

        tab_aggiungi_veicolo = TabAggiungiVeicolo(self, app=container)
        self.add(tab_aggiungi_veicolo, text="Aggiungi Veicolo")
