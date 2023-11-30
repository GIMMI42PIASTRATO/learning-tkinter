# https://www.pythontutorial.net/tkinter/tkinter-grid/ Per spiegazioni sulle grid

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("240x100")
root.title("Length Converter")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# input and unit of measurement
lenght_entry = ttk.Entry(root)
lenght_entry.grid(column=1, row=0)
