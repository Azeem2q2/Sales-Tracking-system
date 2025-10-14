"""This class is your warehouse manager. It keeps track of all products, lets you add,
update, remove, and view them. It uses a dictionary to store products by their ID. from product import Product"""


from product import Product

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, stock):
        if product_id in self.products:
            print(f"Product ID {product_id} already exists.")
            return
        self.products[product_id] = Product(product_id, name, price, stock)
        print(f"Product '{name}' added successfully!")

    def update_product(self, product_id, name=None, price=None, stock=None):
        product = self.products.get(product_id)
        if not product:
            print(f"Product ID {product_id} not found.")
            return
        if name: product.name = name
        if price: product.price = price
        if stock is not None: product.stock = stock
        print(f"Product '{product_id}' updated.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product {product_id} removed.")
        else:
            print(f"Product ID {product_id} not found.")

    def list_products(self):
        if not self.products:
            print("Inventory is empty.")
        for p in self.products.values():
            print(f"ID: {p.product_id}, Name: {p.name}, Price: ₹{p.price}, Stock: {p.stock}")

    def get_product(self, product_id):
        return self.products.get(product_id)
