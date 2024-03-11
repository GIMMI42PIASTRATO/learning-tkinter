from classes.veicolo import Veicolo


class Autocarro(Veicolo):
    def __init__(
        self,
        targa: str,
        marca: str,
        modello: str,
        n_posti: int,
        prezzo_base: float,
        max_carico: float,
    ) -> None:
        super().__init__(targa, marca, modello, n_posti, prezzo_base)
        self.set_max_carico(max_carico)

    def __str__(self) -> str:
        return f"{super().__str__()} - Autocarro - {self.get_prezzo()}€"

    def set_max_carico(self, valore: float):
        if valore > 0:
            self.__max_carico = valore
        else:
            raise ValueError("Il carico massimo deve essere maggiore di zero")

    def get_prezzo(self):
        return self.get_prezzo_base() * self.get_max_carico()

    def get_max_carico(self):
        return self.__max_carico
    
    def get_tipo(self):
        return "Autocarro"
