class Product:
    def __init__(self, name, product_id):
        self.name = name
        self.product_id = product_id
        self.status = "active"

    def create_product(self):
        print(f"Product '{self.name}' created with ID {self.product_id}.")

    def update_product(self, new_name):
        self.name = new_name
        print(f"Product ID {self.product_id} updated to {self.name}.")

    def suspend_product(self):
        self.status = "suspended"
        print(f"Product '{self.name}' has been suspended.")
