import tkinter as tk
from tkinter import ttk


class Memory(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row=0, column=0, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        Memory.label = ttk.Label(
            self,
            text="M",
            background="#202020",
            font="Helvetica",
            width=300,
            foreground="#202020",
        )

        Memory.label.grid(row=0, column=0)

    @staticmethod
    def activate():
        Memory.label["foreground"] = "white"

    @staticmethod
    def deactivate():
        Memory.label["foreground"] = "#202020"
