from products.base_product import BaseProduct


class Lure(BaseProduct):
    def __init__(self, name:str,  quantity:int,brand:str, gram:float, millimeter:float, color:str):
        super().__init__(name, 16, quantity)
        self.color = color
        self.millimeter = millimeter
        self.gram = gram
        self.brand = brand


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value:str):

        if value.strip() == "":
            raise ValueError("Color cannot be empty")

        self.__color = value

    @property
    def millimeter(self):
        return self.__millimeter

    @millimeter.setter
    def millimeter(self, value):
        if value <= 0.0:
            raise ValueError("Millimeter cannot be 0 or negative number")
        self.__millimeter = value

    @property
    def gram(self):
        return self.__gram

    @gram.setter
    def gram(self, value):
        if value <= 0.0:
            raise ValueError("Gram cannot be 0 or negative number")
        self.__gram = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value:str):
        if value.strip() == "":
            raise ValueError("Brand cannot be empty")
        self.__brand = value

    def product_information(self):
        return f"brand:{self.brand}, Name:{self.name}, Gram:{self.gram},millimeter:{self.millimeter} ,Color:{self.color}"


