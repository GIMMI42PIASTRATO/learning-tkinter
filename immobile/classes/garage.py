from classes.immobile import Immobile

class Garage(Immobile):
    def __init__(self, codice, estensione, costo_m2, tax_pct, interrato) -> None:
        super().__init__(codice, estensione, costo_m2, tax_pct)
        self.set_interrato(interrato)

    def __str__(self) -> str:
        return f"{super().__str__()}\ninterrato: {self.get_interrato()}"
    
    def set_interrato(self, interrato):
        self.__interrato = interrato

    def get_interrato(self):
        return self.__interrato