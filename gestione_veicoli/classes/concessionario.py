import typing

# Importing classes
from classes.autocarro import Autocarro
from classes.autoveicolo import Autoveicolo
from classes.motoveicolo import Motoveicolo


class Concessionario:
    def __init__(
        self,
        nome: str,
        indirizzo: str,
        citta: str,
        cap: int,
        provincia: str,
        telefono: str,
        email: str,
    ) -> None:
        self.set_nome(nome)
        self.set_indirizzo(indirizzo)
        self.set_citta(citta)
        self.set_cap(cap)
        self.set_provincia(provincia)
        self.set_telefono(telefono)
        self.set_email(email)
        self.__veicoli = [
            Autocarro("2347834", "Tesla", "Model X", 5, 1000, 5),
            Autoveicolo("1234567", "Fiat", "Panda", 5, 1000, 5),
            Motoveicolo("3434343", "Ducati", "Monster", 2, 1000, 2),
        ]
        self.__veicoli_filtrati = self.__veicoli
        self.__conteggio_veicoli = len(self.__veicoli_filtrati)

    def __str__(self) -> str:
        return f"{self.__nome} - {self.__citta} ({self.__provincia}) - {self.__telefono} - {self.__email} - {len(self.__veicoli)} veicoli"

    def get_nome(self):
        return self.__nome

    def get_indirizzo(self):
        return self.__indirizzo

    def get_citta(self):
        return self.__citta

    def get_cap(self):
        return self.__cap

    def get_provincia(self):
        return self.__provincia

    def get_telefono(self):
        return self.__telefono

    def get_email(self):
        return self.__email

    def get_veicoli(self):
        return self.__veicoli

    #* Get veicoli filtrati
    def get_veicoli_filtrati(self):
        return self.__veicoli_filtrati

    def get_conteggio_veicoli(self):
        return self.__conteggio_veicoli

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_indirizzo(self, indirizzo: str):
        self.__indirizzo = indirizzo

    def set_citta(self, citta: str):
        self.__citta = citta

    def set_cap(self, cap: int):
        self.__cap = cap

    def set_provincia(self, provincia: str):
        self.__provincia = provincia

    def set_telefono(self, telefono: str):
        self.__telefono = telefono

    def set_email(self, email: str):
        self.__email = email

    def set_veicoli(
        self, veicoli: list[typing.Union["Autocarro", "Autoveicolo", "Motoveicolo"]]
    ):
        self.__veicoli = veicoli

    # # Metodi gestione Veicoli
    # def stampa_veicoli(self):
    #     # TODO implementa il metodo per funzionare sulla GUI
    #     for veicolo in self.__veicoli:
    #         print(veicolo)

    # def stampa_numero_veicoli(self):
    #     # TODO implementa il metodo per funzionare sulla GUI
    #     print(len(self.__veicoli))

    # # Metodi gestione Autoveicoli
    # def stampa_autoveicoli(self):
    #     # TODO implementa il metodo per funzionare sulla GUI
    #     for veicolo in self.__veicoli:
    #         if isinstance(veicolo, Autoveicolo):
    #             print(veicolo)

    # def stampa_numero_autoveicoli(self):
    #     # TODO implementa il metodo per funzionare sulla GUI
    #     count = 0
    #     for veicolo in self.__veicoli:
    #         if isinstance(veicolo, Autoveicolo):
    #             count += 1
    #     print(count)

    # # Metodi gestione Autocarri
    # def stampa_autocarri(self):
    #     # TODO implementa il metodo per funzionare sulla GUI
    #     for veicolo in self.__veicoli:
    #         if isinstance(veicolo, Autocarro):
    #             print(veicolo)

    # def stampa_numero_autocarri(self):
    #     # TODO implementa il metodo per funzionare sulla GUI
    #     count = 0
    #     for veicolo in self.__veicoli:
    #         if isinstance(veicolo, Autocarro):
    #             count += 1
    #     print(count)

    # # Metodi gestione Motoveicoli
    # def stampa_motoveicoli(self):
    #     # TODO implementa il metodo per funzionare sulla GUI
    #     for veicolo in self.__veicoli:
    #         if isinstance(veicolo, Motoveicolo):
    #             print(veicolo)

    # def stampa_numero_motoveicoli(self):
    #     # TODO implementa il metodo per funzionare sulla GUI
    #     count = 0
    #     for veicolo in self.__veicoli:
    #         if isinstance(veicolo, Motoveicolo):
    #             count += 1
    #     print(count)

    # Stampa veicolo data la targa
    def stampa_veicolo(self, targa: str):
        # TODO implementa il metodo per funzionare sulla GUI
        veicolo_trovato = False
        for veicolo in self.__veicoli:
            if veicolo.get_targa() == targa:
                print(veicolo)
                veicolo_trovato = True

        if not veicolo_trovato:
            print(f"Veicolo non trovato con targa: {targa}")

    # Aggiungi veicolo
    def aggiungi_veicolo(
        self, veicolo: typing.Union["Autocarro", "Autoveicolo", "Motoveicolo"]
    ):
        # TODO implementa il metodo per funzionare sulla GUI
        self.__veicoli.append(veicolo)
        self.__conteggio_veicoli += 1

    # Rimuovi veicolo
    def rimuovi_veicolo(
        self, veicolo: typing.Union["Autocarro", "Autoveicolo", "Motoveicolo"]
    ):
        # TODO implementa il metodo per funzionare sulla GUI
        self.__veicoli.remove(veicolo)
        self.__conteggio_veicoli -= 1

    #* Set filtro veicoli
    def set_filtro_veicoli(self, tipo_veicolo):
        if tipo_veicolo is None:
            self.__veicoli_filtrati = self.__veicoli
        else:
            tipo_vel = {
                "Autoveicoli": Autoveicolo,
                "Autocarri": Autocarro,
                "Motoveicoli": Motoveicolo,
            }[tipo_veicolo]

            self.__veicoli_filtrati = [
                veicolo for veicolo in self.__veicoli if isinstance(veicolo, tipo_vel)
            ]

        self.__conteggio_veicoli = len(self.__veicoli_filtrati)
