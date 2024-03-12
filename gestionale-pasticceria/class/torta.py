from dolce import Dolce


class Torta(Dolce):

    allergeni_torte = ["uova", "zucchero", "crema", "noci", "anacardi", "uvetta"]

    def __init__(
        self,
        nome: str,
        desc: str,
        peso: float,
        prezzo: float,
        ingredienti: list[str],
        temp_conservazione: float,
    ) -> None:
        super().__init__(nome, desc, peso, prezzo, ingredienti)
        self.set_temp_conservazione(temp_conservazione)
        self.set_allergeni()

    def set_temp_conservazione(self, value: float):
        self.__temp_conservazione = value

    def set_allergeni(self):
        self.__allergeni = []
        for ingrediente in self.get_ingredienti():
            if ingrediente in Torta.allergeni_torte:
                self.__allergeni.append(ingrediente)

    def get_temp_conservazione(self):
        return self.__temp_conservazion

    def get_allergeni(self):
        return self.__allergeni


test = Torta(
    "Torta di bonemeel",
    "Classica torta di minecraft",
    40.5,
    5.5,
    ["uova", "zucchero", "bonemeel", "uvetta"],
    5.5,
)
print(test.get_allergeni())
