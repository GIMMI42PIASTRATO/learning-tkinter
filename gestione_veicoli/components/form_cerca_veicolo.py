from customtkinter import *

class FormCercaVeicolo(CTkFrame):
    def __init__(self, container, app, **kwargs):
        super().__init__(container, **kwargs)
        self.grid(row=0, column=1, sticky="nsew", padx=(0, 30), pady=30)
        self.columnconfigure(1, weight=2)

        self.concessionaria = app.concessionaria
        self.update_img = container.update_img
        self.update_info = container.update_info
        self.remove_info = container.remove_info

        self.create_widgets()

    def create_widgets(self):
    
        # Create the widgets
        self.cerca_veicolo_label = CTkLabel(self, text="Inserisci veicolo")
        self.cerca_veicolo_entry = CTkEntry(self, placeholder_text="Inserisci la targa del veicolo")
        self.error_label = CTkLabel(self, text_color="red", text="")
        self.cerca_button = CTkButton(self, text="Cerca veicolo", command=self.on_click)
        # Bind the enter key to the entry
        self.cerca_veicolo_entry.bind("<Return>", lambda e: self.on_click())

        # Place the widgets in the form
        self.cerca_veicolo_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.cerca_veicolo_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
        self.error_label.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.cerca_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=30)

    def on_click(self):
        targa = self.cerca_veicolo_entry.get()
        print(targa)
        if len(targa) == 7:
            veicolo = self.concessionaria.restituisci_veicolo(targa)
            if veicolo:
                self.error_label.configure(text="")
                self.update_img(veicolo.get_tipo())
                self.update_info(veicolo)

            else:
                self.error_label.configure(text="Veicolo non trovato")
                self.remove_info()
        else:
            self.error_label.configure(text="Targa non valida")
            self.remove_info()
        