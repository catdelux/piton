class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def is_available(self, amount):
        return self.quantity >= amount
    
    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.quantity -= amount
            return True
        return False
    
    def __str__(self):
        return f"{self.name} - {self.price}$ ({self.quantity} in stock)"

class Cart:
    def __init__(self):
        self.items = {}
    
    def add_product(self, product, amount):
        if product.is_available(amount):
            if product.name in self.items:
                self.items[product.name]['quantity'] += amount
            else:
                self.items[product.name] = {'product': product, 'quantity': amount}
            product.reduce_stock(amount)
            print(f"Added {amount}x {product.name} to cart.")
        else:
            print(f"Not enough stock for {product.name}.")
    
    def remove_product(self, product_name, amount):
        if product_name in self.items:
            if self.items[product_name]['quantity'] > amount:
                self.items[product_name]['quantity'] -= amount
            else:
                del self.items[product_name]
            print(f"Removed {amount}x {product_name} from cart.")
        else:
            print(f"{product_name} is not in the cart.")
    
    def total_price(self):
        return sum(item['product'].price * item['quantity'] for item in self.items.values())
    
    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            for item in self.items.values():
                print(f"{item['quantity']}x {item['product'].name} - {item['product'].price}$ each")
            print(f"Total: {self.total_price()}$")

product1 = Product("Laptop", 1000, 5)
product2 = Product("Mouse", 50, 10)

cart = Cart()
cart.add_product(product1, 1)
cart.add_product(product2, 2)
cart.show_cart()
cart.remove_product("Mouse", 1)
cart.show_cart()
