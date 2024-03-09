import tkinter as tk
from tkinter import ttk
import time


class OptionMenu(ttk.OptionMenu):
    def __init__(self, container, options: list[str], concessionaria, tab_veicoli):

        self.container = container
        self.options = options
        self.option_var = tk.StringVar()
        self.concessionaria = concessionaria

        super().__init__(
            container,
            self.option_var,
            self.options[0],
            *self.options,
            command=self.option_changed
        )
        self.grid(row=0, column=2, sticky="e", padx=(0, 10))

    def option_changed(self, event):
        if self.option_var.get() == "Tutti":
            self.concessionaria.set_filtro_veicoli(None)
        else:
            self.concessionaria.set_filtro_veicoli(self.option_var.get())
            
        self.container.update_numero_veicoli()

