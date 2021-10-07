from products import Products
class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        price = input(f"Enter Price for {new_product}: $")
        price = float(price)
        category = input("Enter Category: ")
        new_product = Products(new_product, price, category)
        self.products.append(new_product)

    def sell_product(self, id):
        print(market.products[id].print_info())
        market.products.pop(id)

market = Store("Bargain Market")
market.add_product("Eggs")
market.add_product("Steak")
market.sell_product(0)
print(market.products[0].name)