from person.person import Person
from products.base_product import BaseProduct



class Customer(Person):
    def __init__(self, name, person_id, phone, balance):
        super().__init__(name, person_id, phone)
        self.orders:list = []
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be 0 or negative number")

        self.__balance = value


    def add_order(self, product:BaseProduct):
        self.orders.append(product)


    def person_information(self):
        return f"Customer: {self.name}, ID: {self.person_id}, Phone: {self.phone}"



