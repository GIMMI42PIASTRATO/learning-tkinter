import tkinter as tk
from tkinter import ttk
from customtkinter import *
from PIL import ImageTk, Image

# Importing components
from components.form import Form


class TabAggiungiVeicolo(CTkFrame):
    def __init__(self, container, app):
        super().__init__(container, fg_color="#1c1c1c")
        self.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)

        self.app = app

        self.create_widgets()

    def create_widgets(self):
        # Create the widgets
        self.img = CTkFrame(self, fg_color="white", corner_radius=15, width=300, height=300)
        self.form = Form(self, app=self.app, fg_color="#2b2b2b", corner_radius=15)

        # Place the widgets
        self.img.grid(row=0, column=0, sticky="n",padx=30, pady=30)
        self.form.grid(row=0, column=1, sticky="nsew", pady=30, padx=(0, 30))
