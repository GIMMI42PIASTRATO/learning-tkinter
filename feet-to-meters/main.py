from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Length Converter")

main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

length1 = StringVar()
length1_entry = ttk.Entry(main_frame, width=7, textvariable=length1)
length1_entry.grid(column=2, row=1, sticky=(W, E))

length2 = StringVar()
ttk.Entry(main_frame, width=7, textvariable=length2).grid(
    column=2, row=2, sticky=(W, E)
)

ttk.Button(main_frame, text="Calculate").grid(column=3, row=3, sticky=W)

from_unit_combobox = ttk.Combobox(
    main_frame,
    width=7,
    values=["meter", "kilometer", "decimeter", "centimeter", "millimeter", "feet"],
)
from_unit_combobox.grid(column=3, row=1, sticky=W)
from_unit_combobox.current(5)

ttk.Label(main_frame, text="is equivalent to").grid(column=1, row=2, sticky=E)

to_unit_combobox = ttk.Combobox(
    main_frame,
    width=7,
    values=["meter", "kilometer", "decimeter", "centimeter", "millimeter", "feet"],
)
to_unit_combobox.grid(column=3, row=2, sticky=W)
to_unit_combobox.current(0)

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

length1_entry.focus()
# root.bind("<Return>", )

mainloop()
