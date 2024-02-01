import tkinter as tk
from tkinter import ttk

# Components import
from components.Display import DisplayFrame
from components.Numpad import NumpadFrame
from components.Memory import Memory


class App(tk.Tk):
    def __init__(self) -> None:
        # Inizzializzazione della finestra root
        super().__init__()
        self.title("Calculator")
        self.geometry("350x525")
        self.resizable(False, False)

        # Renderizzazione dei componenti
        self.display = DisplayFrame(container=self)
        self.numpad = NumpadFrame(container=self)
        self.memory = Memory(container=self)

    def onClick(self):
        print("Hello World")


if __name__ == "__main__":
    app = App()
    app.mainloop()
