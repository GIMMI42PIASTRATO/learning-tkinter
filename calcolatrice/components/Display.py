import tkinter as tk
from tkinter import ttk


class DisplayFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row=0, column=0)

        self.create_widgets()

    def create_widgets(self):
        # Create the widgets
        display = tk.Text(
            self, width=300, height=1, font=("Helvetica", 32), state="disabled"
        )

        # Place the widgets
        display.grid(row=0, column=0)
