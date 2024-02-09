from dolce import Dolce

class PastaFresca(Dolce):
    
    allergeni_paste = ["uova", "zucchero", "crema", "noci", "anacardi", "uvetta", "confettura di fragole", "confettura di mirtillo", "confettura di albicocca", "liquore"]
    
    def __init__(self, nome: str, desc: str, peso: float, prezzo: float, ingredienti: list[str]) -> None:
        super().__init__(nome, desc, peso, prezzo, ingredienti)
        self.set_allergeni()
        
    def set_allergeni(self):
        self.__allergeni = []
        for ingrediente in self.get_ingredienti():
            if ingrediente in PastaFresca.allergeni_paste:
                self.__allergeni.append(ingrediente)         
        