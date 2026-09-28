from person.customer import Customer
from products.base_product import BaseProduct


class FishingShop:
    def __init__(self):
        self.products:list[BaseProduct] = []
        self.customers:list[Customer] = []
        self.income = 0


    def add_product(self, product:BaseProduct):
        self.products.append(product)

    def add_customer(self, customer:Customer):
        for c in self.customers:
            if c.person_id == customer.person_id:
                return 'this id is used'

        self.customers.append(customer)
        return 'you have successfully added'

    def find_product(self, product_name):

        product = next(( p for p in self.products if p.name == product_name), None)

        if product:
            return product.product_information()

        return 'this product not found'

    def sell_product(self, customer_id, product_name,quantity):
        customer = next((c for c in self.customers if c.person_id == customer_id), None)
        product = next((p for p in self.products if p.name == product_name),None)
        if not customer or not product:
            return 'there is no customer or product'

        if product.quantity < quantity:
            return 'there is not a sufficient quantity'

        if customer.balance < product.price * quantity:
            return f"{customer.name} nor enough money"

        total_price = product.price * quantity

        customer.balance -= total_price
        product.quantity -= quantity
        customer.add_order(product)
        self.income += total_price

    def find_customer(self, customer_id):
        customer = next((c for c in self.customers if c.person_id == customer_id), None)
        if not customer:
            return "customer not found"
        return customer.person_information()