#Simple E-commerce system
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    def __str__(self):
        return f"{self.id}: {self.name} - ${self.price:.2f} (Stock: {self.stock})"
class ShoppingCart:
    def __init__(self):
        self.items = {}
    def add_item(self, product, quantity):
        if product.stock >= quantity:
            if product.name in self.items:
                self.items[product.id]['quantity'] += quantity
            else:
                self.items[product.id] = {'product': product, 'quantity': quantity}
            product.stock -= quantity
            print(f"Added {quantity} of {product.id} to the cart.")
        else:
            print(f"Not enough stock for {product.id}. Available: {product.stock}")
    def remove_item(self, product_id):
        if product_id in self.items:
            product = self.items[product_id]['product']
            product.stock += self.items[product_id]['quantity']
            del self.items[product_id]
            print(f"Removed {product.id} from the cart.")
        else:
            print("Item not found in the cart.")
    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("Your Shopping Cart:")
        total = 0
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            total += product.price * quantity
            print(f"{product.name} - ${product.price:.2f} x {quantity} = ${product.price * quantity:.2f}")
        print(f"Total: ${total:.2f}")
class ECommerceSystem:
    def __init__(self):
        self.products = []
        self.cart = ShoppingCart()
    def add_product(self, product):
        self.products.append(product)
    def view_products(self):
        print("Available Products:")
        for product in self.products:
            print(product)
    def checkout(self):
        total = sum(item['product'].price * item['quantity'] for item in self.cart.items.values())
        print(f"Your total is: ${total:.2f}")
        print("Thank you for your purchase!")
def main():
    system = ECommerceSystem()
    system.add_product(Product(1, "Samsung F23 5g ", 999.99, 50))
    system.add_product(Product(2, "Samsung S25", 499.99, 10))
    system.add_product(Product(3, "Phone Covers", 199.99, 150))
    while True:
        print("\n1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            system.view_products()
        elif choice == '2':
            product_id = int(input("Enter product id to add to cart: "))
            quantity = int(input("Enter quantity: "))
            product = next((p for p in system.products if p.id == product_id), None)
            if product:
                system.cart.add_item(product, quantity)
            else:
                print("Product not found.")
        elif choice == '3':
            product_id = int(input("Enter product id to remove from cart: "))
            system.cart.remove_item(product_id)
        elif choice == '4':
            system.cart.view_cart()
        elif choice == '5':
            system.cart.view_cart()
            system.checkout()
            break
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()