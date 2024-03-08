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
        self.veicoli_filtrati = self.veicoli

        self.conteggio_veicoli = len(self.veicoli_filtrati)

    def add_veicolo(self, veicolo):
        self.veicoli.append(veicolo)
        self.conteggio_veicoli += 1

    def remove_veicolo(self, veicolo):
        self.veicoli.remove(veicolo)
        self.conteggio_veicoli -= 1

    def get_veicoli(self):
        return self.veicoli

    def set_filtro_veicoli(self, tipo_veicolo):
        if tipo_veicolo is None:
            self.veicoli_filtrati = self.veicoli
        else:
            tipo_vel = {
                "Autoveicoli": Autoveicolo,
                "Autocarri": Autocarro,
                "Motoveicoli": Motoveicolo,
            }[tipo_veicolo]

            self.veicoli_filtrati = [
                veicolo for veicolo in self.veicoli if isinstance(veicolo, tipo_vel)
            ]

        self.conteggio_veicoli = len(self.veicoli_filtrati)
