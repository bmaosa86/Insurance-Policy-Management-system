class Policyholder:
    def __init__(self, name, policyholder_id):
        self.name = name
        self.policyholder_id = policyholder_id
        self.status = "active"
        self.products = []
        self.payment_status = {}

    def register(self):
        print(f"Policyholder {self.name} has been registered.")

    def suspend(self):
        self.status = "suspended"
        print(f"Policyholder {self.name} has been suspended.")

    def reactivate(self):
        self.status = "active"
        print(f"Policyholder {self.name} has been reactivated.")

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added to {self.name}'s account.")

    def display_details(self):
        print(f"Policyholder: {self.name} (ID: {self.policyholder_id})")
        print(f"Status: {self.status}")
        print(f"Products: {[product.name for product in self.products]}")
        print(f"Payment Status: {self.payment_status}")
