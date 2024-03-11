from customtkinter import *

class Form(CTkFrame):
    def __init__(self, container, app, **kwargs):
        super().__init__(container, **kwargs)
        self.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(1, weight=2)

        self.concessionaria = app.concessionaria

        self.create_widgets()

    def create_widgets(self):

        # Create the widgets
        self.tipo_veicolo_label = CTkLabel(self, text="Tipo veicolo: ")
        self.tipo_veicolo_option_menu = CTkOptionMenu(self, values=["Autoveicoli", "Autocarri", "Motoveicoli"], command=self.option_changed)

        self.targa_label = CTkLabel(self, text="Targa: ")
        self.targa_entry = CTkEntry(self, placeholder_text="Inserisci la targa del veicolo")

        self.marca_label = CTkLabel(self, text="Marca: ")
        self.marca_entry = CTkEntry(self, placeholder_text="Inserisci la marca del veicolo")

        self.modello_label = CTkLabel(self, text="Modello: ")
        self.modello_entry = CTkEntry(self, placeholder_text="Inserisci il modello del veicolo")

        self.numero_posti_label = CTkLabel(self, text="Numero posti: ")
        self.numero_posti_entry = CTkEntry(self, placeholder_text="Inserisci il numero di posti del veicolo")

        self.prezzo_base_label = CTkLabel(self, text="Prezzo base: ")
        self.prezzo_base_entry = CTkEntry(self, placeholder_text="Inserisci il prezzo base del veicolo")

        self.variable_label = CTkLabel(self, text="Numero porte: ")
        self.variable_entry = CTkEntry(self, placeholder_text="Inserisci il numero di porte del veicolo")


        # Place the widgets in the form
        self.tipo_veicolo_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.tipo_veicolo_option_menu.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        self.targa_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.targa_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

        self.marca_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.marca_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        self.modello_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.modello_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=10)

        self.numero_posti_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)
        self.numero_posti_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=10)

        self.prezzo_base_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)
        self.prezzo_base_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=10)

        self.variable_label.grid(row=6, column=0, sticky="w", padx=10, pady=10)
        self.variable_entry.grid(row=6, column=1, sticky="ew", padx=10, pady=10)


    def option_changed(self, event):
        if self.tipo_veicolo_option_menu.get() == "Autoveicoli":
            self.variable_label.configure(text="Numero porte: ")
            self.variable_entry.configure(placeholder_text="Inserisci il numero di porte del veicolo")
        elif self.tipo_veicolo_option_menu.get() == "Autocarri":
            self.variable_label.configure(text="Capacità di carico: ")
            self.variable_entry.configure(placeholder_text="Inserisci la capacità di carico del veicolo")
        else:
            self.variable_label.configure(text="Cilindrata: ")
            self.variable_entry.configure(placeholder_text="Inserisci la cilindrata del veicolo")
