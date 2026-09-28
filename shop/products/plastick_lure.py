from products.base_product import BaseProduct


class PlasticLure(BaseProduct):
    def __init__(self, name:str,  quantity:int , brand:str ,millimeter:float, gram:float, color:str):
        super().__init__(name, 10, quantity)
        self.color = color
        self.gram = gram
        self.millimeter = millimeter
        self.brand = brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: str):

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
    def brand(self, value: str):
        if value.strip() == "":
            raise ValueError("Brand cannot be empty")
        self.__brand = value

    def product_information(self):
        return f"brand:{self.brand}, Name:{self.name}, Gram:{self.gram},millimeter:{self.millimeter} ,Color:{self.color}"
