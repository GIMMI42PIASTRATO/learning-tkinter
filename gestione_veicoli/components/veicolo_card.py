from tkinter import ttk
from PIL import ImageTk, Image


class Card(ttk.Frame):
    def __init__(self, container, veicolo, row: int, column: int):
        super().__init__(container)
        self.grid(row=row, column=column, sticky="nsew")

        self.veicolo = veicolo
        self.img = ImageTk.PhotoImage(Image.open("gestione_veicoli/image/bugatti.png").resize((200, 200)))
        self.create_widgets()

    def create_widgets(self):
        # Image
        self.image = ttk.Label(self, image=self.img)
        self.image.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # Marca e Modello
        self.title = ttk.Label(self, text=f"{self.veicolo.get_marca()} {self.veicolo.get_modello()}")
        self.title.grid(row=1, column=0, sticky="nsew")

        # Tipo di veicolo
        self.description = ttk.Label(self, text="Un bel veicolo")
        self.description.grid(row=2, column=0, sticky="nsew")

        # Price
        self.price = ttk.Label(self, text=self.veicolo.get_prezzo())
        self.price.grid(row=3, column=0, sticky="nsew")