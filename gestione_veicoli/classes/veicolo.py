from abc import ABC, abstractclassmethod


class Veicolo(ABC):
    def __init__(
        self, targa: str, marca: str, modello: str, n_posti: int, prezzo_base: float
    ) -> None:
        self.set_targa(targa)
        self.set_marca(marca)
        self.set_modello(modello)
        self.set_numero_posti(n_posti)
        self.set_prezzo_base(prezzo_base)

    def __str__(self) -> str:
        return f"{self.get_marca()} - {self.get_modello()}"

    def set_targa(self, valore: str):
        if len(valore) == 7:
            self.__targa = valore
        else:
            raise ValueError("La targa deve avere una lunghezza di 7 caratteri")

    def set_marca(self, valore: str):
        self.__marca = valore

    def set_modello(self, valore: str):
        self.__modello = valore

    def set_numero_posti(self, valore: int):
        if valore > 0:
            self.__numero_posti = valore
        else:
            raise ValueError("Il numero di posti deve essere maggiore di zero")

    def set_prezzo_base(self, prezzo_base: float):
        if prezzo_base <= 0:
            raise ValueError("Il prezzo base deve essere maggiore di zero")

        self.__prezzo_base = prezzo_base

    def get_targa(self):
        return self.__targa

    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_numero_posti(self):
        return self.__numero_posti

    def get_prezzo_base(self):
        return self.__prezzo_base

    @abstractclassmethod
    def get_prezzo(self):
        pass
