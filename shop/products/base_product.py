from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str):
        if value.strip() == "":
            raise ValueError("The name is mandatory and cannot be empty")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("The price cannot be a negative number or 0")
        self.__price = value


    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("The quantity cannot be a negative number or 0")

        self.__quantity = value

    @abstractmethod
    def product_information(self):
        pass

    def add_product(self, amound):
        if amound <= 0:
            raise ValueError("Amount must be positive")

        self.__quantity += amound

    def sell_product(self, amound):
        if amound <= 0:
            raise ValueError("amound must be positive")

        if amound < self.__quantity:
            self.__quantity -= amound

        if amound > self.__quantity:
            raise ValueError("There arent many products")
