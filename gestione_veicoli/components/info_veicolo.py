from customtkinter import *

class InfoVeicolo(CTkFrame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=30)

        self.create_widgets()

    def create_widgets(self):
        self.info_marca = CTkLabel(self, text="")
        self.info_modello = CTkLabel(self, text="")
        self.info_tipo_veicolo = CTkLabel(self, text="")
        self.info_numero_posti = CTkLabel(self, text="")
        self.info_prezzo_base = CTkLabel(self, text="")
        self.info_variable = CTkLabel(self, text="")
        self.info_targa = CTkLabel(self, text="")

    def display_info(self, veicolo):
        # Place the widgets in the form
        self.info_marca.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.info_modello.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        self.info_tipo_veicolo.grid(row=0, column=2, sticky="w", padx=10, pady=10)
        self.info_numero_posti.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.info_prezzo_base.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        self.info_variable.grid(row=1, column=2, sticky="w", padx=10, pady=10)
        self.info_targa.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        # Set the text of the labels
        if veicolo.get_tipo() == "Autoveicolo":
            text = ["Numero porte:", veicolo.get_numero_porte]
        elif veicolo.get_tipo() == "Autocarro":
            text = ["Carico massimo:", veicolo.get_max_carico]
        else:
            text = ["Cilindrata:", veicolo.get_cilindrata]

        self.info_marca.configure(text=f"Marca: {veicolo.get_marca()}")
        self.info_modello.configure(text=f"Modello: {veicolo.get_modello()}")
        self.info_tipo_veicolo.configure(text=f"Tipo veicolo: {veicolo.get_tipo()}")
        self.info_numero_posti.configure(text=f"Numero posti: {veicolo.get_numero_posti()}")
        self.info_prezzo_base.configure(text=f"Prezzo base: {veicolo.get_prezzo_base()}")
        self.info_variable.configure(text=f"{text[0]} {text[1]()}")
        self.info_targa.configure(text=f"Targa: {veicolo.get_targa()}")





