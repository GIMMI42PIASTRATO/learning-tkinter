import sys
import os

# Adding the path to the sys.path
current_dir = os.path.dirname(__file__)
gestione_veicoli_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(gestione_veicoli_dir)

# Component Imports
from classes.autoveicolo import Autoveicolo
from classes.autocarro import Autocarro
from classes.motoveicolo import Motoveicolo


class Concessionaria:
    def __init__(self) -> None:
        self.veicoli = [
            Autocarro("2347834", "Tesla", "Model X", 5, 1000, 5),
            Autoveicolo("1234567", "Fiat", "Panda", 5, 1000, 5),
            Motoveicolo("3434343", "Ducati", "Monster", 2, 1000, 2),
        ]

        self.conteggio_veicoli = len(self.veicoli)

    def add_veicolo(self, veicolo):
        self.veicoli.append(veicolo)
        self.conteggio_veicoli += 1

    def remove_veicolo(self, veicolo):
        self.veicoli.remove(veicolo)
        self.conteggio_veicoli -= 1

    def get_veicoli(self):
        return self.veicoli
