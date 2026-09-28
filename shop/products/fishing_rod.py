from products.base_product import BaseProduct


class FishingRod(BaseProduct):
    def __init__(self, name:str,  quantity:int, brand:str, meter:int, action:float, weight:int):
        super().__init__(name, 90, quantity)
        self.weight = weight
        self.action = action
        self.meter = meter
        self.brand = brand

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value:int):
        if value <= 0:
            raise ValueError("weight cannot be 0 or negative number")

        self.__weight = value

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value:float):

        if value <= 0.0:
            raise ValueError("action cannot be 0 or negative number")

        self.__action = value


    @property
    def meter(self):
        return self.__meter

    @meter.setter
    def meter(self, value):
        if value <= 0:
            raise ValueError("meter cannot be 0 or negative number")

        self.__meter = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value:str):
        if value.strip() == "":
            raise ValueError("brand cannot be empty")
        self.__brand = value

    def product_information(self):
        return f"rod brand:{self.brand}, rod name:{self.name},meter:{self.meter} ,weight:{self.weight}, action:{self.action}"
