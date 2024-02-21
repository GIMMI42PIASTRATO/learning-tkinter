class Immobile:
    def __init__(self, codice, estensione, costo_m2, tax_pct) -> None:
        self.inserisci(codice, estensione, costo_m2, tax_pct)

    def __str__(self) -> str:
        return f"codice: {self.get_codice()}\nestensione: {self.get_estensione()}\ncosto: {self.get_costo()}\npercentuale tasse: {self.get_percentuale_tasse}"

    # setter e getter

    def set_codice(self, codice):
        self.__codice = codice

    def set_estensione(self, estensione):
        if estensione <= 0:
            raise ValueError
        self.__estensione = estensione

    def set_costo_m2(self, costo_m2):
        if costo_m2 <= 0:
            raise ValueError
        self.__costo = costo_m2

    def set_percentuale_tasse(self, tax_pct):
        if tax_pct <= 0:
            raise ValueError
        self.__percetuale_tasse = tax_pct

    def get_codice(self):
        return self.__codice

    def get_estensione(self):
        return self.__estensione

    def get_costo_m2(self):
        return self.__costo

    def get_percentuale_tasse(self):
        return self.__percetuale_tasse

    def inserisci(self, codice, estensione, costo_m2, tax_pct):
        self.set_codice(codice)
        self.set_estensione(estensione)
        self.set_costo_m2(costo_m2)
        self.set_percentuale_tasse(tax_pct)

    def calcola_valore(self):
        return self.get_costo_m2 * self.get_estensione()

    def calcola_tassa(self):
        return (self.calcola_valore * self.get_percentuale_tasse) / 100
