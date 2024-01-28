import tkinter as tk
from tkinter import ttk
from helper.Calculator import Calculator


# TODO Rinomina il file chiamandolo Numpad. Questo componente ciclera sulla classe button e li passera varie informazioni, questa classe sara anche quella che permette la renderizzazione di tutti i bottoni


class NumpadFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row=1, column=0, sticky="nsew")
        self.calculator = Calculator()

        self.create_widgets(container)

    def create_widgets(self, container):
        buttons_text = [
            "MEM",
            "STO",
            "M+",
            "C",
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "0",
            ".",
            "+",
            "=",
        ]
        print(len(buttons_text))

        for i in range(5):
            for j in range(4):
                print(f"i * 4 + j = {i * 4 + j}")
                button_text_value = buttons_text[i * 4 + j]
                button = ttk.Button(self, text=buttons_text[i * 4 + j])
                button.bind(
                    "<Button-1>",
                    lambda event: self.onClick(event, container),
                )

                # Se il bottone cliccato non e un bottone correlato a quelli della memoria allora binda il bottone alla pressione del testo relativo al bottone stesso es: tasto 0 bindato a <KeyPress-0>
                # if button_text_value.isnumeric() or button_text_value in [
                #     "+",
                #     "-",
                #     "*",
                #     "/",
                #     ".",
                # ]:
                #     container.bind(
                #         f"<KeyPress>",
                #         lambda event, value=button_text_value: print(value),
                #     )

                button.grid(row=i, column=j, sticky="nsew")

    def onClick(self, event, container):
        display_text = container.display.label["text"]
        btn_text = event.widget["text"]

        if btn_text.isnumeric():
            if (
                display_text == "0"
                or display_text == "0.0"
                or display_text == "Syntax Error"
            ):
                container.display.label["text"] = btn_text
            else:
                container.display.label["text"] += btn_text

        elif btn_text in ["+", "-", "*", "/"]:
            if display_text[-1] in ["+", "-", "*", "/"]:
                # L'implementazione commentata è superiore, ma il compito richiede di mostrare l'errore
                # container.display.label["text"] = display_text[:-1] + btn_text
                container.display.label["text"] = "Syntax Error"
            else:
                result = self.calculator.solve_expression(display_text)
                if not result:
                    container.display.label["text"] += btn_text
                else:
                    container.display.label["text"] = str(result) + btn_text

        elif btn_text == ".":
            if "." not in display_text:
                container.display.label["text"] += btn_text

        elif btn_text == "C":
            self.calculator.clear()
            container.display.label["text"] = "0"

        # Calculations

        elif btn_text == "=":
            pass
