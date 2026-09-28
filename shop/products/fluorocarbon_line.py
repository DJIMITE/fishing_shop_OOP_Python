from products.base_product import BaseProduct


class Fluorocarbon(BaseProduct):
    def __init__(self, name:str,  quantity:int, brand:str, diameter:float, meter:int, strength:float):
        super().__init__(name, 8.90, quantity)
        self.strength = strength
        self.meter = meter
        self.diameter = diameter
        self.brand = brand


    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0.0:
            raise ValueError("strength cannot be 0 or negative number")

        self.__strength = value

    @property
    def meter(self):
        return self.__meter

    @meter.setter
    def meter(self, value):
        if value <= 0:
            raise  ValueError("meter cannot be 0 or negative number")
        self.__meter = value


    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        if value <= 0.0:
            raise ValueError("diameter cannot be 0 or negative number")

        self.__diameter = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value:str):
        if value.strip() == "":
            raise ValueError("brand cannot be empty")

        self.__brand = value

    def product_information(self):
        return f"Brand:{self.brand}, Name:{self.name}, Diameter:{self.diameter}, Strength:{self.strength}, Meter:{self.meter}"