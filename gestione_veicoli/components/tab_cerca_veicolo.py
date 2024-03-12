from customtkinter import *
from PIL import ImageTk, Image

class TabCercaVeicolo(CTkFrame):
    def __init__(self, container, app):
        super().__init__(container, fg_color="#1c1c1c")
        self.grid(row=0, column=0, sticky="nsew")

        self.app = app

        self.create_widgets()

    def create_widgets(self):
        self.img = CTkLabel(self, image=ImageTk.PhotoImage(Image.open("gestione_veicoli\image\No-Image-Placeholder.png")), fg_color="white", corner_radius=15, width=300, height=300)
        self.img.grid(row=0, column=0, sticky="n",padx=30, pady=30)

    def update_img(self, type):
        img_path = {
            "Autoveicolo": "",
            "Autocarro": "",
            "Motoveicolo": "",
        }[None]

        img = ImageTk.PhotoImage(Image.open(img_path).resize((300, 300)))

        self.img.config(image=img_path)
        