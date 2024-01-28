import math


class Calculator:
    def __init__(self) -> None:
        self.__previous_number = None
        self.__current_number = None
        self.__num_list = None
        self.__operator = None
        self.__result = None

    def __str__(self) -> str | None:
        return f"Previous number: {self.__previous_number}\nCurrent number: {self.__current_number}\nOperator: {self.__operator}"

    def solve_expression(self, expression: str) -> float:
        self.__num_list = self.__split_expression(expression)
        self.__current_number = float(self.__num_list[-1])

        if self.__previous_number == None:
            self.__previous_number = self.__current_number
            return None
        else:
            operators = ["+", "-", "*", "/"]
            for operator in operators:
                if operator in expression:
                    self.__operator = operator

            compute = {
                "+": self.__add,
                "-": self.__subtract,
                "*": self.__multiply,
                "/": self.__divide,
            }[self.__operator]

            self.__result = compute()

            self.__previous_number = self.__result

            return self.__result

    def equals(self, expression: str) -> float:
        self.__num_list = self.__split_expression(expression)
        self.__current_number = float(self.__num_list[-1])
        return self.__result

    # Calculations

    def __add(self) -> float:
        return self.__previous_number + self.__current_number

    def __subtract(self) -> float:
        return self.__previous_number - self.__current_number

    def __multiply(self) -> float:
        return self.__previous_number * self.__current_number

    def __divide(self) -> float:
        if self.__current_number == 0:
            raise ZeroDivisionError
        else:
            return self.__previous_number / self.__current_number

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
        self.__result = None
