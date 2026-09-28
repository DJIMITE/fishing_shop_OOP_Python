from person.customer import Customer
from products.fishing_rod import FishingRod
from products.braided_line import BraidedLine
from products.fluorocarbon_line import Fluorocarbon
from products.lure import Lure
from products.plastick_lure import PlasticLure
from products.spinner import Spinner
from shop import FishingShop


shop = FishingShop()


# Customers
customer1 = Customer("Ivan", "12345678", "0888123456", 200)
customer2 = Customer("Petar", "87654321", "0899123456", 50)

shop.add_customer(customer1)
shop.add_customer(customer2)


# Products
rod = FishingRod("Spinning Rod",  10, "Shimano", 2.40, 3, 150)
line = BraidedLine("Power Pro",  20, "PowerPro", 0.16, 150, "Green")
fluoro = Fluorocarbon("Fluoro",  15, "Seaguar", 0.20, 50, 5)
lure = Lure("Minnow", 10, "Rapala", 15, 100, "Silver")
plastic_lure = PlasticLure("Soft Bait",  20, "Savage Gear", 80, 10, "Red")
spinner = Spinner("Spinner 1", 15, "Mepps", 10, "Silver")


shop.add_product(rod)
shop.add_product(line)
shop.add_product(fluoro)
shop.add_product(lure)
shop.add_product(plastic_lure)
shop.add_product(spinner)


# Test find product
print(shop.find_product("Spinning Rod"))

# Test find customer
print(shop.find_customer("12345678"))


# Test selling
print("\nBefore sale:")
print("Customer balance:", customer1.balance)
print("Rod quantity:", rod.quantity)
print("Shop income:", shop.income)


shop.sell_product("12345678", "Spinning Rod", 2)


print("\nAfter sale:")
print("Customer balance:", customer1.balance)
print("Rod quantity:", rod.quantity)
print("Shop income:", shop.income)
print("Orders:", ", ".join(p.name for p in customer1.orders))