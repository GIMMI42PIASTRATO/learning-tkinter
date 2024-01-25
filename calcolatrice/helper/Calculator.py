import math


class Calculator:
    def __init__(self) -> None:
        self.__memory = 0
        self.__result = 0

    # Getters and Setters

    def getMemory(self):
        return self.__memory

    def setMemory(self, value):
        self.__memory = value

    def getResult(self):
        return self.__result

    def setResult(self, value):
        self.__result = value

    # Operations

    # Options

    def reset(self):
        self.__result = 0
        self.__isResult = False

    def clear(self):
        self.__result = 0
        self.__isResult = False
        self.__operation = None
