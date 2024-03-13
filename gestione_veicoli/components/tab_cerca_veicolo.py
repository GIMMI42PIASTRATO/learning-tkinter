from customtkinter import *
from PIL import ImageTk, Image

class TabCercaVeicolo(CTkFrame):
    def __init__(self, container, app):
        super().__init__(container, fg_color="#1c1c1c")
        self.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(1, weight=2)

        self.app = app

        self.create_widgets()

    def create_widgets(self):

        # Creating the image
        self.img = CTkLabel(self, image=ImageTk.PhotoImage(Image.open("gestione_veicoli/image/No-Image-Placeholder.png").resize((300, 300))), corner_radius=15)

        # Creating the form frame
        #TODO TRASFORMA IN UNA CLASSE
        self.cerca_veicolo_form = CTkFrame(self, fg_color="#2b2b2b")
        self.cerca_veicolo_form.columnconfigure(1, weight=2)

        self.cerca_veicolo_label = CTkLabel(self.cerca_veicolo_form, text="Inserisci veicolo")
        self.cerca_veicolo_entry = CTkEntry(self.cerca_veicolo_form, placeholder_text="Inserisci la targa del veicolo")
        self.cerca_button = CTkButton(self.cerca_veicolo_form, text="Cerca veicolo", command=self.on_click)

        # Placing widgets
        self.img.grid(row=0, column=0, sticky="n",padx=15, pady=30)
        self.cerca_veicolo_form.grid(row=0, column=1, sticky="nsew", padx=(0, 30), pady=30)
        self.cerca_veicolo_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.cerca_veicolo_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
        self.cerca_button.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=30)

        self.update_img("Autoveicolo")

    def update_img(self, type):
        img_path = {
            "Autoveicolo": "gestione_veicoli/image/bugatti.png",
            "Autocarro": "",
            "Motoveicolo": "",
        }[type]

        new_img = ImageTk.PhotoImage(Image.open(img_path).resize((300, 300)))

        self.img.configure(image=new_img, text="")

    def on_click(self, event):
        print("Ok")
        