from abc import ABC, abstractclassmethod


class Dolce(ABC):
    def __init__(
        self, nome: str, desc: str, peso: float, prezzo: float, ingredienti: list[str]
    ) -> None:
        self.set_nome(nome)
        self.set_descrizione(desc)
        self.set_peso(peso)
        self.set_prezzo(prezzo)
        self.set_ingredienti(ingredienti)

    def __str__(self) -> str:
        return f"nome: {self.__nome}\ndescrizione: {self.__descrizione}\npeso: {self.__peso}\nprezzo: {self.__prezzo}\ningredienti: {self.__ingredienti}"

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_descrizione(self, desc: str):
        self.__descrizione = desc

    def set_peso(self, peso: float):
        self.__peso = peso

    def set_prezzo(self, prezzo: float):
        self.__prezzo = prezzo

    def set_ingredienti(self, ingredienti: list[str]):
        self.__ingredienti = ingredienti

    @abstractclassmethod
    def set_allergeni(self):
        pass

    def get_nome(self):
        return self.__nome

    def get_descrizione(self):
        return self.__descrizione

    def get_peso(self):
        return self.__peso

    def get_prezzo(self):
        return self.__prezzo

    def get_ingredienti(self):
        return self.__ingredienti

    @abstractclassmethod
    def get_allergeni(self):
        pass
