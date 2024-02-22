from classes.immobile import Immobile

class Alloggio(Immobile):
    def __init__(self, codice, estensione, costo_m2, tax_pct, vani_stanze) -> None:
        super().__init__(codice, estensione, costo_m2, tax_pct)
        self.set_vani_stanze(vani_stanze)

    def __str__(self) -> str:     
        return f"{super().__str__()}\nvani e stanze: {self.get_vani_stanze()}"
    
    def set_vani_stanze(self, vani_stanze):
        if vani_stanze <= 0:
            raise ValueError
        self.__vani_stanze = vani_stanze

    def get_vani_stanze(self):
        return self.__vani_stanze