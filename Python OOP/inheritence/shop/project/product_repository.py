from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
            return product
        except StopIteration:
            pass

    def remove(self, product_name):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        result = '\n'.join([f'{p.name}: {p.quantity}' for p in self.products])

        return result
