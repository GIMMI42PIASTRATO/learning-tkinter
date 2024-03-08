from classes.veicolo import Veicolo


class Autoveicolo(Veicolo):
    def __init__(
        self,
        targa: str,
        marca: str,
        modello: str,
        n_posti: int,
        prezzo_base: float,
        numero_porte: int,
    ) -> None:
        super().__init__(targa, marca, modello, n_posti, prezzo_base)
        self.set_numero_porte(numero_porte)

    def __str__(self) -> str:
        return f"{super().__str__()} - Autoveicolo - {self.get_numero_porte()} porte"

    def set_numero_porte(self, numero_porte: int):
        if numero_porte <= 0:
            raise ValueError("Il numero di porte deve essere maggiore di zero")

        self.__numero_porte = numero_porte

    def get_numero_porte(self):
        return self.__numero_porte

    def get_prezzo(self):
        return self.get_prezzo_base() * self.get_numero_porte()
