from veicolo import Veicolo


class Autocarro(Veicolo):
    def __init__(
        self, targa: str, marca: str, modello: str, n_posti: int, prezzo_base: float
    ) -> None:
        super().__init__(targa, marca, modello, n_posti, prezzo_base)
