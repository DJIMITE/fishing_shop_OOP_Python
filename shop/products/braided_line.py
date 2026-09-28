from products.base_product import BaseProduct


class BraidedLine(BaseProduct):
    def __init__(self, name, quantity,brand, pe:float, meter:int, color:str,):
        super().__init__(name, 19, quantity)
        self.brand = brand
        self.color = color
        self.meter = meter
        self.pe = pe
    
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, value:str):
        if value.strip() == "":
            raise ValueError("Brand cannot be empty")

        self.__brand = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value:str):
        if value.strip() == '':
            raise ValueError("Color cannot be empty")

        self.__color = value

    @property
    def meter(self):
        return self.__meter

    @meter.setter
    def meter(self, value):
        if value <=0:
            raise ValueError("Meter must be greater than 0")

        self.__meter = value

    @property
    def pe(self):
        return self.__pe

    @pe.setter
    def pe(self, value):
        if value <= 0:
            raise ValueError("PE must be greater than 0")
        self.__pe = value

    def product_information(self):
        return f'Brand: {self.brand}, Name: {self.name}, PE: {self.pe}, Meter: {self.meter}, Color: {self.color}'
