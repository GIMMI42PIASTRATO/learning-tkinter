from customtkinter import *

# Importing classes
from classes.autoveicolo import Autoveicolo
from classes.autocarro import Autocarro
from classes.motoveicolo import Motoveicolo

class Form(CTkFrame):
    def __init__(self, container, app, notebook, **kwargs):
        super().__init__(container, **kwargs)
        self.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(1, weight=2)

        self.concessionaria = app.concessionaria
        self.notebook = notebook

        self.create_widgets()

    def create_widgets(self):

        # Create the widgets
        self.tipo_veicolo_label = CTkLabel(self, text="Tipo veicolo: ")
        self.tipo_veicolo_option_menu = CTkOptionMenu(
            self,
            values=["Autoveicoli", "Autocarri", "Motoveicoli"],
            command=self.option_changed,
        )

        self.targa_label = CTkLabel(self, text="Targa: ")
        self.targa_entry = CTkEntry(
            self, placeholder_text="Inserisci la targa del veicolo"
        )

        self.marca_label = CTkLabel(self, text="Marca: ")
        self.marca_entry = CTkEntry(
            self, placeholder_text="Inserisci la marca del veicolo"
        )

        self.modello_label = CTkLabel(self, text="Modello: ")
        self.modello_entry = CTkEntry(
            self, placeholder_text="Inserisci il modello del veicolo"
        )

        self.numero_posti_label = CTkLabel(self, text="Numero posti: ")
        self.numero_posti_entry = CTkEntry(
            self, placeholder_text="Inserisci il numero di posti del veicolo"
        )

        self.prezzo_base_label = CTkLabel(self, text="Prezzo base: ")
        self.prezzo_base_entry = CTkEntry(
            self, placeholder_text="Inserisci il prezzo base del veicolo"
        )

        self.variable_label = CTkLabel(self, text="Numero porte: ")
        self.variable_entry = CTkEntry(
            self, placeholder_text="Inserisci il numero di porte del veicolo"
        )

        self.crea_veicolo_btn = CTkButton(self, text="Crea veicolo", command=self.create_veicolo)
        self.error_label = CTkLabel(self, text="", text_color="red")

        # Place the widgets in the form
        self.tipo_veicolo_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.tipo_veicolo_option_menu.grid(
            row=0, column=1, sticky="ew", padx=10, pady=10
        )

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

        self.crea_veicolo_btn.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        self.error_label.grid(row=8, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        

    def option_changed(self, event):
        if self.tipo_veicolo_option_menu.get() == "Autoveicoli":
            self.variable_label.configure(text="Numero porte: ")
            self.variable_entry.configure(
                placeholder_text="Inserisci il numero di porte del veicolo"
            )
        elif self.tipo_veicolo_option_menu.get() == "Autocarri":
            self.variable_label.configure(text="Capacità di carico: ")
            self.variable_entry.configure(
                placeholder_text="Inserisci la capacità di carico del veicolo"
            )
        else:
            self.variable_label.configure(text="Cilindrata: ")
            self.variable_entry.configure(
                placeholder_text="Inserisci la cilindrata del veicolo"
            )

    def get_values(self):
        return {
            "targa": self.targa_entry.get(),
            "marca": self.marca_entry.get(),
            "modello": self.modello_entry.get(),
            "numero_posti": self.numero_posti_entry.get(),
            "prezzo_base": self.prezzo_base_entry.get(),
            "variable": self.variable_entry.get(),
        }
    
    def clear(self):
        self.targa_entry.delete(0, "end")
        self.marca_entry.delete(0, "end")
        self.modello_entry.delete(0, "end")
        self.numero_posti_entry.delete(0, "end")
        self.prezzo_base_entry.delete(0, "end")
        self.variable_entry.delete(0, "end")

    def check_values(self):
        values = self.get_values()
        if "" in values.values():
            return False
        
        if len(values["targa"]) != 7:
            return False
        
        if not values["numero_posti"].isdigit():
            return False

        if not float(values["prezzo_base"]) > 0:
            return False
        
        if not float(values["variable"]) > 0:
            return False

        return True
    
    def create_veicolo(self):
        if self.check_values():
            self.error_label.configure(text="")
            values = self.get_values()
            if self.tipo_veicolo_option_menu.get() == "Autoveicoli":
                veicolo = Autoveicolo(
                    values["targa"],
                    values["marca"],
                    values["modello"],
                    int(values["numero_posti"]),
                    float(values["prezzo_base"]),
                    int(values["variable"]),
                )
                self.add_veicolo(veicolo)

            elif self.tipo_veicolo_option_menu.get() == "Autocarri":
                veicolo = Autocarro(
                    values["targa"],
                    values["marca"],
                    values["modello"],
                    int(values["numero_posti"]),
                    float(values["prezzo_base"]),
                    float(values["variable"]),
                )
                self.add_veicolo(veicolo)

            else:
                veicolo = Motoveicolo(
                    values["targa"],
                    values["marca"],
                    values["modello"],
                    int(values["numero_posti"]),
                    float(values["prezzo_base"]),
                    int(values["variable"]),
                )
                self.add_veicolo(veicolo)

            self.clear()
        else:
            self.error_label.configure(text="Errore: I valori inseriti non sono validi")

    def add_veicolo(self, veicolo):
        self.concessionaria.aggiungi_veicolo(veicolo)
        self.notebook.refresh()