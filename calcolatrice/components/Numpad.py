import tkinter as tk
from tkinter import Misc, ttk
from helper.Calculator import Calculator


# TODO rendi il Bottone un componente separato passandoli come props il testo e il bind


class NumpadFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row=2, column=0, sticky="nsew")
        self.calculator = Calculator()

        self.create_widgets(container)

        self.n_root_active = False

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
                    button.grid(row=i, column=j, sticky="nsew", ipadx=5, ipady=25)

    def display_nums(self, container):
        if (
            self.display_text == "0"
            or self.display_text == "0.0"
            or self.display_text == "Syntax Error"
            or self.display_text == "Math Error"
        ):
            container.display.label["text"] = self.btn_text
        elif self.n_root_active:
            container.display.label["text"] = self.btn_text + self.display_text
        else:
            container.display.label["text"] += self.btn_text

    def operators_err(self, container):
        if self.display_text[-1] in ["+", "-", "*", "/"]:
            # L'implementazione commentata è superiore, ma il compito richiede di mostrare l'errore
            # container.display.label["text"] = display_text[:-1] + btn_text
            self.calculator.clear()
            container.display.label["text"] = "Syntax Error"
        else:
            container.display.label["text"] += self.btn_text

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

    def decimal_point(self, container):
        if "." not in self.display_text:
            container.display.label["text"] += self.btn_text

    def delete(self, container):
        self.calculator.clear()
        container.display.label["text"] = self.display_text[:-1]
        if len(container.display.label["text"]) == 0:
            container.display.label["text"] = "0"

    def equal(self, container):
        if self.display_text == "Syntax Error" or self.display_text == "Math Error":
            container.display.label["text"] = "0"
        elif "^" in self.display_text:
            self.n_exponent(container)
        elif "\u221A" in self.display_text:
            self.n_root_active = False
            self.n_root(container)
        else:
            try:
                result = self.calculator.equals(self.display_text)
                # TODO codice per implementazione senza funzione eval()
                # result = self.calculator.solve_expression(display_text)
                container.display.label["text"] = str(result)
            except ZeroDivisionError:
                self.calculator.clear()
                container.display.label["text"] = "Math Error"
            except SyntaxError:
                self.calculator.clear()
                container.display.label["text"] = "Syntax Error"

    def sin(self, container):
        self.equal(container)
        try:
            result = self.calculator.sin(float(container.display.label["text"]))
            container.display.label["text"] = str(result)
        except:
            container.display.label["text"] = "Syntax Error"

    def cos(self, container):
        self.equal(container)
        try:
            result = self.calculator.cos(float(container.display.label["text"]))
            container.display.label["text"] = str(result)
        except ValueError:
            container.display.label["text"] = "Syntax Error"

    def tan(self, container):
        self.equal(container)
        try:
            result = self.calculator.tan(float(container.display.label["text"]))
            container.display.label["text"] = str(result)
        except ValueError:
            container.display.label["text"] = "Syntax Error"
        except Exception:
            container.display.label["text"] = "Math Error"

    def square(self, container):
        self.equal(container)
        try:
            result = self.calculator.square(float(container.display.label["text"]))
            container.display.label["text"] = str(result)
        except ValueError:
            container.display.label["text"] = "Syntax Error"

    def n_exponent(self, container):
        if "^" in self.display_text:
            try:
                number, exponent = map(float, self.display_text.split("^"))
                result = self.calculator.n_exponent(number, exponent)
                container.display.label["text"] = str(result)
            except ValueError:
                container.display.label["text"] = "Syntax Error"
        else:
            self.equal(container)
            container.display.label["text"] += "^"

    def sqrt(self, container):
        self.equal(container)
        try:
            result = self.calculator.sqrt(float(container.display.label["text"]))
            container.display.label["text"] = str(result)
        except ValueError:
            container.display.label["text"] = "Syntax Error"
        except Exception:
            container.display.label["text"] = "Math Error"

    def n_root(self, container):
        if "\u221A" in self.display_text:
            self.n_root_active = False
            try:
                exponent, base = map(float, self.display_text.split("\u221A"))
                result = self.calculator.n_root(base, exponent)
                container.display.label["text"] = str(result)
            except ValueError:
                container.display.label["text"] = "Syntax Error"
            except Exception:
                container.display.label["text"] = "Math Error"
        else:
            self.equal(container)
            container.display.label["text"] = "\u221A" + container.display.label["text"]
            self.n_root_active = True

    def factorial(self, container):
        self.equal(container)
        try:
            result = self.calculator.factorial(int(container.display.label["text"]))
            container.display.label["text"] = str(result)
        except ValueError:
            container.display.label["text"] = "Syntax Error"
        except Exception:
            container.display.label["text"] = "Math Error"

    def mutual(self, container):
        self.equal(container)
        try:
            result = self.calculator.mutual(float(container.display.label["text"]))
            container.display.label["text"] = str(result)
        except ValueError:
            container.display.label["text"] = "Syntax Error"
        except Exception:
            container.display.label["text"] = "Math Error"

    def onClick(self, event, container):
        self.display_text = container.display.label["text"]
        self.btn_text = event.widget["text"]

        if self.display_text == "Syntax Error" or self.display_text == "Math Error":
            container.display.label["text"] = "0"
            return

        # Display numbers

        if self.btn_text.isnumeric():
            self.display_nums(container)

        # Syntax Errors

        elif self.btn_text in ["+", "-", "*", "/"]:
            self.operators_err(container)

        # Decimal point

        elif self.btn_text == ".":
            self.decimal_point(container)

        elif self.btn_text == "C":
            self.delete(container)

        # Calculations

        elif self.btn_text == "=":
            self.equal(container)

        elif self.btn_text == "sin":
            self.sin(container)

        elif self.btn_text == "cos":
            self.cos(container)

        elif self.btn_text == "tan":
            self.tan(container)

        # TODO sec csc

        elif self.btn_text == "x^2":
            self.square(container)

        elif self.btn_text == "x^n":
            self.n_exponent(container)

        elif self.btn_text == "\u221A":
            self.sqrt(container)

        elif self.btn_text == "\u02E3\u221A":
            self.n_root(container)

        elif self.btn_text == "n!":
            self.factorial(container)

        elif self.btn_text == "1/n":
            self.mutual(container)

        # Memory
        elif self.btn_text == "STO":
            try:
                self.calculator.save_in_memory(float(self.display_text[-1]))
            except ValueError:
                container.display.label["text"] = "Syntax Error"

        elif self.btn_text == "MEM":
            container.display.label["text"] = str(self.calculator.read_memory())

        elif self.btn_text == "M+":
            self.calculator.add_to_memory(float(self.display_text))
