import tkinter as tk
from tkinter import ttk

# Components import
from components.Display import DisplayFrame


class App(tk.Tk):
    def __init__(self) -> None:
        # Inizzializzazione della finestra root
        super().__init__()
        self.title("Calculator")
        self.geometry("400x300")
        self.minsize(400, 300)

        # Renderizzazione dei componenti
        self.display = DisplayFrame(container=self)

    def onClick(self):
        print("Hello World")


if __name__ == "__main__":
    app = App()
    app.mainloop()
