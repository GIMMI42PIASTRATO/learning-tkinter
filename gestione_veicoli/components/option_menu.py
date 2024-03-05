import tkinter as tk
from tkinter import ttk


class OptionMenu(ttk.OptionMenu):
    def __init__(self, container, options: list[str]):

        self.container = container
        self.options = options
        self.option_var = tk.StringVar()

        super().__init__(
            container,
            self.option_var,
            self.options[0],
            *self.options,
            command=self.option_changed
        )
        self.grid(row=0, column=2, sticky="e", padx=(0, 10))

    def option_changed(self, event):
        print(self.option_var.get())
