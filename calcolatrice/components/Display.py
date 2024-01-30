import tkinter as tk
from tkinter import ttk


class DisplayFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(
            row=1,
            column=0,
        )

        self.create_widgets()

    def create_widgets(self):
        # Create the widgets
        self.label = ttk.Label(
            self,
            width=300,
            font=("Helvetica", 32),
            text="0",
            background="#202020",
            foreground="white",
        )

        # Place the widgets
        self.label.grid(row=0, column=0)
