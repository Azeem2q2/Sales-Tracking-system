from inventory_manager import InventoryManager
from sales_manager import SalesManager
from reports import generate_inventory_report, generate_sales_report
from exceptions import OutOfStockError
from reports import generate_inventory_report, generate_sales_report

def main():
    inventory = InventoryManager()
    sales = SalesManager(inventory)

    while True:
        print("\n Menu:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. List Inventory")
        print("5. Record Sale")
        print("6. View Sales")
        print("7. Reports")
        print("0. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                pid = input("Product ID: ")
                name = input("Name: ")
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                inventory.add_product(pid, name, price, stock)

            elif choice == "2":
                pid = input("Product ID to update: ")
                name = input("New Name (or leave blank): ")
                price = input("New Price (or leave blank): ")
                stock = input("New Stock (or leave blank): ")
                inventory.update_product(pid,
                    name=name if name else None,
                    price=float(price) if price else None,
                    stock=int(stock) if stock else None)

            elif choice == "3":
                pid = input("Product ID to remove: ")
                inventory.remove_product(pid)

            elif choice == "4":
                inventory.list_products()

            elif choice == "5":
                pid = input("Product ID to sell: ")
                qty = int(input("Quantity: "))
                try:
                    sales.record_sale(pid, qty)
                except OutOfStockError as e:
                    print(f"{e}")

            elif choice == "6":
                sales.list_sales()

            elif choice == "7":
                generate_inventory_report(inventory)
                generate_sales_report(sales)

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
