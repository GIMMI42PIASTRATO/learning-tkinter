import tkinter as tk
from tkinter import ttk

# Components import


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculator")
        self.geometry("400x300")

    def onClick(self):
        print("Hello World")


if __name__ == "__main__":
    app = App()
    app.mainloop()
