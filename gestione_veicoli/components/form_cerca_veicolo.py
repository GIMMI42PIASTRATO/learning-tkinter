from customtkinter import *

class FormCercaVeicolo(CTkFrame):
    def __init__(self, container, app, **kwargs):
        super().__init__(container, **kwargs)
        self.grid(row=0, column=1, sticky="nsew", padx=(0, 30), pady=30)
        self.columnconfigure(1, weight=2)

        self.concessionaria = app.concessionaria
        self.update_img = container.update_img

        self.create_widgets()

    def create_widgets(self):
    
        # Create the widgets
        self.cerca_veicolo_label = CTkLabel(self, text="Inserisci veicolo")
        self.cerca_veicolo_entry = CTkEntry(self, placeholder_text="Inserisci la targa del veicolo")
        self.cerca_button = CTkButton(self, text="Cerca veicolo", command=self.on_click)

        # Place the widgets in the form
        self.cerca_veicolo_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.cerca_veicolo_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
        self.cerca_button.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=30)

    def on_click(self):
        print("Cliccato")
        # targa = self.cerca_veicolo_entry.get()
        # veicolo = self.concessionaria.cerca_veicolo(targa)
        # self.master.master.update_img(veicolo.tipo)