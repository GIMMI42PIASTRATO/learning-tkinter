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
        separators = ["+", "-", "*", "/"]
        for separator in separators:
            string = " ".join(expression.split(separator))
            if " " in string:
                break

        self.__num_list = string.split()
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
            return self.__result

    def __add(self) -> float:
        return self.__previous_number + self.__current_number

    def __subtract(self) -> float:
        return self.__previous_number - self.__current_number

    def __multiply(self) -> float:
        return self.__previous_number * self.__current_number

    def __divide(self) -> float:
        return self.__previous_number / self.__current_number
