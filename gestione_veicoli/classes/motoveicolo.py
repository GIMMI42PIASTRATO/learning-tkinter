from classes.veicolo import Veicolo


class Motoveicolo(Veicolo):
    def __init__(
        self,
        targa: str,
        marca: str,
        modello: str,
        n_posti: int,
        prezzo_base: float,
        cilindrata: int,
    ) -> None:
        super().__init__(targa, marca, modello, n_posti, prezzo_base)
        self.set_cilindrata(cilindrata)

    def __str__(self) -> str:
        return f"{super().__str__()} - Motoveicolo - {self.get_prezzo()}€"

    def set_cilindrata(self, valore: int):
        if valore > 0:
            self.__cilindrata = valore
        else:
            raise ValueError("La cilindrata deve essere maggiore di zero")

    def get_cilindrata(self):
        return self.__cilindrata

    def get_prezzo(self):
        return self.get_prezzo_base() * self.get_cilindrata()
    
    def get_tipo(self):
        return "Motoveicolo"
