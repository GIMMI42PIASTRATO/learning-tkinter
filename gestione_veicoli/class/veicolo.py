from abc import ABC, abstractclassmethod


class Veicolo(ABC):
    def __init__(self, targa: str, marca: str, modello: str, n_posti: int) -> None:
        self.set_targa(targa)
        self.set_marca(marca)
        self.set_modello(modello)
        self.set_numero_posti(n_posti)

    def __str__(self) -> str:
        return f"{self.get_marca()} - {self.get_modello}"

    def set_targa(self, valore: str):
        if len(valore) == 7:
            self.__targa = valore
        else:
            raise ValueError

    def set_marca(self, valore: str):
        self.__marca = valore

    def set_modello(self, valore: str):
        self.__modello = valore

    def set_numero_posti(self, valore: int):
        if valore > 0:
            self.__numero_posti = valore
        else:
            raise ValueError

    @abstractclassmethod
    def set_prezzo(self, prezzo_base: float):
        pass

    def get_targa(self):
        return self.__targa

    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_numero_posti(self):
        return self.__numero_posti

    @abstractclassmethod
    def get_prezzo(self):
        pass
