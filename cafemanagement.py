class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CafeManagementSystem:
    def __init__(self):
        self.menu = []
        self.orders = []
    
    def add_menu_item(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)
        print(f"{name} added to the menu.")
    
    def display_menu(self):
        print("\nMenu:")
        for i, item in enumerate(self.menu, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")
    
    def take_order(self):
        self.display_menu()
        order = []
        while True:
            try:
                choice = int(input("\nEnter the menu item number to add to the order (0 to finish): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(self.menu):
                    item = self.menu[choice - 1]
                    order.append(item)
                    print(f"{item.name} added to the order.")
                else:
                    print("Invalid choice, please select a valid menu item.")
            except ValueError:
                print("Please enter a valid number.")
        
        self.orders.append(order)
    
    def generate_bill(self):
        total = 0
        print("\nBill:")
        for order in self.orders:
            for item in order:
                print(f"{item.name} - ${item.price:.2f}")
                total += item.price
        print(f"\nTotal amount: ${total:.2f}")

# Sample usage
if __name__ == "__main__":
    system = CafeManagementSystem()
    
    # Add items to the menu
    system.add_menu_item("Coffee", 3.00)
    system.add_menu_item("Tea", 2.50)
    system.add_menu_item("Sandwich", 5.50)
    system.add_menu_item("Cake", 4.00)
    
    # Take orders
    system.take_order()
    
    # Generate bill
    system.generate_bill()
