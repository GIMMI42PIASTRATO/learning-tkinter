import tkinter as tk
from tkinter import ttk
from helper.Calculator import Calculator


# TODO rendi il Bottone un componente separato passandoli come props il testo e il bind


class NumpadFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row=2, column=0, sticky="nsew")
        self.calculator = Calculator()

        self.create_widgets(container)

    def create_widgets(self, container):
        buttons_text = [
            "MEM",
            "STO",
            "M+",
            "C",
            "CE",
            "sin",
            "cos",
            "tan",
            "sec",
            "csc",
            "x^2",
            "x^n",
            "\u221A",
            "\u02E3\u221A",
            "n!",
            "1/n",
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

        for i in range(8):
            for j in range(4):
                print(f"i * 4 + j = {i * 4 + j}")
                button_text_value = buttons_text[i * 4 + j]
                button = ttk.Button(self, text=buttons_text[i * 4 + j])

                button.bind(
                    "<Button-1>",
                    lambda event: self.onClick(event, container),
                )

                # TODO Implementa il bind dei tasti della tastiera
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

                if i < 3:
                    button.grid(row=i, column=j, sticky="nsew", ipadx=5, ipady=5)
                else:
                    button.grid(row=i, column=j, sticky="nsew", ipadx=5, ipady=20)

    def onClick(self, event, container):
        display_text = container.display.label["text"]
        btn_text = event.widget["text"]

        # Display numbers

        if btn_text.isnumeric():
            if (
                display_text == "0"
                or display_text == "0.0"
                or display_text == "Syntax Error"
                or display_text == "Math Error"
            ):
                container.display.label["text"] = btn_text
            else:
                container.display.label["text"] += btn_text

        # Syntax Errors

        elif btn_text in ["+", "-", "*", "/"]:
            if display_text[-1] in ["+", "-", "*", "/"]:
                # L'implementazione commentata è superiore, ma il compito richiede di mostrare l'errore
                # container.display.label["text"] = display_text[:-1] + btn_text
                self.calculator.clear()
                container.display.label["text"] = "Syntax Error"
            else:
                container.display.label["text"] += btn_text

            # TODO codice per implementazione senza funzione eval()
            #     try:
            #         result = self.calculator.solve_expression(display_text)
            #         if not result:
            #             container.display.label["text"] += btn_text
            #         else:
            #             container.display.label["text"] = str(result) + btn_text
            #     except ZeroDivisionError:
            #         self.calculator.clear()
            #         container.display.label["text"] = "Math Error"

        # Decimal point

        elif btn_text == ".":
            if "." not in display_text:
                container.display.label["text"] += btn_text

        elif btn_text == "C":
            self.calculator.clear()
            container.display.label["text"] = display_text[:-1]
            if len(container.display.label["text"]) == 0:
                container.display.label["text"] = "0"

        # Calculations

        elif btn_text == "=":
            try:
                result = self.calculator.equals(display_text)
                # TODO codice per implementazione senza funzione eval()
                # result = self.calculator.solve_expression(display_text)
                container.display.label["text"] = str(result)
            except ZeroDivisionError:
                self.calculator.clear()
                container.display.label["text"] = "Math Error"
            except SyntaxError:
                self.calculator.clear()
                container.display.label["text"] = "Syntax Error"

        # Memory
        elif btn_text == "STO":
            self.calculator.save_in_memory(float(display_text))

        elif btn_text == "MEM":
            container.display.label["text"] = str(self.calculator.read_memory())

        elif btn_text == "M+":
            self.calculator.add_to_memory(float(display_text))
