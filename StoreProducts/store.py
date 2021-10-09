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

    def sell_product(self, productId):
        for item in self.products:
            # print(self.products[item].product_id)
            if item.product_id == productId:
                item.print_info()
                self.products.remove(item)

    def inflation(self, percent_increase):
        for item in self.products:
            item.price += percent_increase*item.price
            print(f"You have increased {item.name} by ${percent_increase*item.price:.2f}")
            item.print_info()

    def clearance(self, percent_decrease, category):
        for item in self.products:
            if item.category == category:
                item.price -= percent_decrease*item.price
                print(f"You have decreased {item.name} by ${percent_decrease*item.price:.2f} in {category}")
                item.print_info()


