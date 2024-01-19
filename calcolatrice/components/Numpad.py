import tkinter as tk
from tkinter import ttk


# TODO Rinomina il file chiamandolo Numpad. Questo componente ciclera sulla classe button e li passera varie informazioni, questa classe sara anche quella che permette la renderizzazione di tutti i bottoni


class NumpadFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row=1, column=0, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        button_text = [
            "MEM",
            "STO",
            "M+",
            "C",
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "0",
            ".",
            "+",
            "=",
        ]
        print(len(button_text))

        for i in range(5):
            for j in range(4):
                print(f"i * 4 + j = {i * 4 + j}")
                button = ttk.Button(self, text=button_text[i * 4 + j])
                button.grid(row=i, column=j, sticky="nsew")
