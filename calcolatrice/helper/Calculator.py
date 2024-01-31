import math
from components.Memory import Memory
from uu import Error


class Calculator:
    def __init__(self) -> None:
        # TODO codice per implementazione senza funzione eval()
        # self.__previous_number = None
        # self.__current_number = None
        # self.__num_list = None

        self.__operator = None
        self.__result = None
        self.__memory = None

    def __str__(self) -> str | None:
        return f"Previous number: {self.__previous_number}\nCurrent number: {self.__current_number}\nOperator: {self.__operator}"

    # Algoritmo per la risoluzione di espressioni matematiche, non funzionante con i numeri negativi, per questioni di tempo quindi utilizzerò la funzione eval() di python, in seguito implementerò l'algoritmo senza l'utilizzo di funzioni già esistenti
    # TODO codice per implementazione senza funzione eval()
    # def solve_expression(self, expression: str) -> float:
    #     self.__num_list = self.__split_expression(expression)
    #     self.__current_number = float(self.__num_list[-1])

    #     if self.__previous_number == None:
    #         self.__previous_number = self.__current_number
    #         return None
    #     else:
    #         operators = ["+", "-", "*", "/"]
    #         for operator in operators:
    #             if operator in expression:
    #                 self.__operator = operator

    #         compute = {
    #             "+": self.__add,
    #             "-": self.__subtract,
    #             "*": self.__multiply,
    #             "/": self.__divide,
    #         }[self.__operator]

    #         self.__result = compute()

    #         self.__previous_number = self.__result

    #         return self.__result

    def equals(self, expression: str) -> float:
        self.__result = eval(expression)
        return self.__result

        # TODO codice per implementazione senza funzione eval()
        # self.__num_list = self.__split_expression(expression)
        # self.__current_number = float(self.__num_list[-1])
        # return self.__result

    # Calculations

    # def __add(self) -> float:
    #     return self.__previous_number + self.__current_number

    # def __subtract(self) -> float:
    #     return self.__previous_number - self.__current_number

    # def __multiply(self) -> float:
    #     return self.__previous_number * self.__current_number

    # def __divide(self) -> float:
    #     if self.__current_number == 0:
    #         raise ZeroDivisionError
    #     else:
    #         return self.__previous_number / self.__current_number

    def sin(self, value: float) -> float:
        return math.sin(math.radians(value))

    def cos(self, value: float) -> float:
        return math.cos(math.radians(value))

    def tan(self, value: float) -> float | None:
        if abs(math.radians(value) % (math.pi / 2)) < 1e-15:
            raise Exception("Math Error")
        else:
            return math.tan(math.radians(value))

    # Helpers

    def __split_expression(self, expression: str) -> list:
        separators = ["+", "-", "*", "/"]
        for separator in separators:
            string = " ".join(expression.split(separator))
            if " " in string:
                break

        return string.split()

    def clear(self) -> None:
        self.__previous_number = None
        self.__current_number = None
        self.__num_list = None
        self.__operator = None
        # self.__result = None

    # STO
    def save_in_memory(self, value: float) -> None:
        if self.__result == None:
            # Numero sullo schermo
            self.__memory = value
        else:
            # Risultato ultima operazione
            self.__memory = self.__result

        if self.__memory != 0 or self.__memory != None:
            # Fa il display della M
            Memory.activate()
        else:
            # Rimuove la M dallo schermo
            Memory.deactivate()

    # MEM
    def read_memory(self) -> float:
        return self.__memory

    # M+
    def add_to_memory(self, value: float) -> None:
        if self.__memory == None:
            # Se nulla è salvato in memoria non fa nulla
            return

        if self.__result == None:
            # Aggiunge numero sullo schermo alla memoria
            self.__memory += value
        else:
            # Aggiunge risultato ultima operazione alla memoria
            self.__memory += self.__result

        if self.__memory != 0:
            # Fa il display della M
            Memory.activate()
        else:
            # Rimuove la M dallo schermo
            Memory.deactivate()
