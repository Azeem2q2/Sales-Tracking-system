from sale import Sale
from exceptions import OutOfStockError

class SalesManager:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager
        self.sales = []

    def record_sale(self, product_id, quantity):
        product = self.inventory.get_product(product_id)
        if not product:
            print(f"❌ Product ID {product_id} not found.")
            return
        if quantity > product.stock:
            raise OutOfStockError(f"Cannot sell {quantity} units. Only {product.stock} left.")
        product.stock -= quantity
        total_price = product.price * quantity
        sale = Sale(product_id, quantity, total_price)
        self.sales.append(sale)
        print(f"✅ Sale recorded: {sale}")

    def list_sales(self):
        if not self.sales:
            print("📭 No sales recorded.")
        for s in self.sales:
            print(s)
