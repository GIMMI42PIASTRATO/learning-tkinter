from tkinter import ttk
from PIL import ImageTk, Image
from customtkinter import CTkFrame


class Card(CTkFrame):
    def __init__(self, container, veicolo, row: int, column: int):
        super().__init__(container)
        self.grid(row=row, column=column, sticky="nsew", padx=25, pady=10)

        self.veicolo = veicolo
        image_path = {
            "Autoveicolo": "gestione_veicoli/image/bugatti.png",
            "Autocarro": "gestione_veicoli/image/truck-slider-dc.png",
            "Motoveicolo": "gestione_veicoli/image/tim-meyer-2LTMNCN4nEg-unsplash.jpg",
        }[veicolo.get_tipo()]
        self.img = ImageTk.PhotoImage(
            Image.open(image_path).resize((200, 200))
        )
        self.create_widgets()

    def create_widgets(self):
        # Image
        self.image = ttk.Label(self, image=self.img)
        self.image.grid(row=0, column=0, sticky="nsew")

        # Marca e Modello
        self.title = ttk.Label(
            self, text=f"{self.veicolo.get_marca()} {self.veicolo.get_modello()}"
        )
        self.title.grid(row=1, column=0, sticky="nsew")

        # Tipo di veicolo
        self.tipo_veicolo = ttk.Label(
            self, text=f"Tipo veicolo: {self.veicolo.get_tipo()}"
        )
        self.tipo_veicolo.grid(row=2, column=0, sticky="nsew")

        # Price
        self.price = ttk.Label(self, text=f"Prezzo: {self.veicolo.get_prezzo()}€")
        self.price.grid(row=3, column=0, sticky="nsew")

        # Targa
        self.targa = ttk.Label(self, text=f"Targa: {self.veicolo.get_targa()}")
        self.targa.grid(row=4, column=0, sticky="nsew")
