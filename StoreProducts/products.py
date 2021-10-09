class Products:
    def __init__(self, name, price = 0, category = ""):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percentage_change, is_increased):
        if is_increased == True:
            self.price += self.price*percentage_change
        else:
            self.price -= self.price*percentage_change
        return self

    def print_info(self):
        print(f"Product: {self.name} \nCategory: {self.category} \nPrice: ${self.price:.2f}")
        # print(self.name, self.price, self.category)
        return self