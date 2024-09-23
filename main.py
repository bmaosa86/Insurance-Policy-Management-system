from policyholder import Policyholder
from product import Product
from payment import Payment

# Create policyholders
policyholder1 = Policyholder("John Doe", 1)
policyholder2 = Policyholder("Jane Smith", 2)

# Register policyholders
policyholder1.register()
policyholder2.register()

# Create a product
life_insurance = Product("Life Insurance", 101)
life_insurance.create_product()

# Assign the product to policyholders
policyholder1.add_product(life_insurance)
policyholder2.add_product(life_insurance)

# Process payments for both policyholders
payment1 = Payment(200, policyholder1)
payment2 = Payment(300, policyholder2)

payment1.process_payment()
payment2.process_payment()

# Display policyholder details
policyholder1.display_details()
policyholder2.display_details()
