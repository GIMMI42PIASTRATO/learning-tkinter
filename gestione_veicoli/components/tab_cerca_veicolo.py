from customtkinter import *
from PIL import ImageTk, Image

# Importing components
from components.form_cerca_veicolo import FormCercaVeicolo
from components.info_veicolo import InfoVeicolo

class TabCercaVeicolo(CTkFrame):
    def __init__(self, container, app):
        super().__init__(container, fg_color="#1c1c1c")
        self.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(1, weight=2)

        self.app = app

        self.create_widgets()

    def create_widgets(self):

        # Creating the image
        self.img = CTkLabel(self, text="", image=ImageTk.PhotoImage(Image.open("gestione_veicoli/image/No-Image-Placeholder.png").resize((300, 300))))

        # Creating the form
        self.form_cerca_veicolo = FormCercaVeicolo(self, self.app, fg_color="#2b2b2b")

        # Creating the info component
        self.info_veicolo = InfoVeicolo(self, fg_color="#2b2b2b")

        # Placing widgets
        self.img.grid(row=0, column=0, sticky="n",padx=15, pady=30)

    def update_img(self, type):
        img_path = {
            "Autoveicolo": "gestione_veicoli/image/bugatti.png",
            "Autocarro": "gestione_veicoli/image/truck-slider-dc.png",
            "Motoveicolo": "gestione_veicoli/image/tim-meyer-2LTMNCN4nEg-unsplash.jpg",
        }[type]

        new_img = ImageTk.PhotoImage(Image.open(img_path).resize((300, 300)))

        self.img.configure(image=new_img, text="")

    def update_info(self, veicolo):
        self.info_veicolo.display_info(veicolo)

    def remove_info(self):
        self.info_veicolo.remove_info()
        self.img.configure(image=ImageTk.PhotoImage(Image.open("gestione_veicoli/image/No-Image-Placeholder.png").resize((300, 300))))