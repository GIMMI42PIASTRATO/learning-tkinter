import tkinter as tk
from tkinter import ttk


# TODO Rinomina il file chiamandolo Numpad. Questo componente ciclera sulla classe button e li passera varie informazioni, questa classe sara anche quella che permette la renderizzazione di tutti i bottoni


class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Opzioni
