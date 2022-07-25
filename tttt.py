#task02

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
        self.amount = None


class ProductStore:
    def __init__(self, *args: Product):
        self.income = 0
        self.all_products = []
        for product in args:
            self.product = product
            self.product.amount = 1
            self.all_products.append(product)
