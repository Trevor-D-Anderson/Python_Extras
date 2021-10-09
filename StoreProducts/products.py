class Products:
    productId = 0

    def __init__(self, name, price = 0, category = ""):
        self.name = name
        self.price = price
        self.category = category
        self.product_id = Products.get_id()

    def update_price(self, percentage_change, is_increased):
        if is_increased == True:
            self.price += self.price*percentage_change
        else:
            self.price -= self.price*percentage_change
        return self

    def print_info(self):
        print(f"Product: {self.name} \nCategory: {self.category} \nPrice: ${self.price:.2f} \nProduct Id: {self.product_id}")
        # print(self.name, self.price, self.category)
        return self

    @classmethod
    def get_id(cls):
        cls.productId += 1
        return cls.productId
