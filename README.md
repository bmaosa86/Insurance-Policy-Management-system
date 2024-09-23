# Insurance-Policy-Management-system

## Overview
This is a Policy Management System that allows policy managers to manage policyholders, products, and payments. The system includes:
- Registration, suspension, and reactivation of policyholders.
- Creation, updating, and suspension of products.
- Payment processing, reminders, and penalty application for late payments.

## How to Run
1. Clone the repository or unzip the project folder.
2. Ensure you have Python installed (version 3.6 or higher).
3. Run the `main.py` file to see the demonstration of the system's functionality.

## Classes and Methods
- `Policyholder`: Handles policyholder management.
  - Methods: `register()`, `suspend()`, `reactivate()`, `add_product()`, `display_details()`
  
- `Product`: Manages insurance products.
  - Methods: `create_product()`, `update_product()`, `suspend_product()`
  
- `Payment`: Processes payments and manages reminders and penalties.
  - Methods: `process_payment()`, `send_reminder()`, `apply_penalty()`

## Demonstration
The system creates two policyholders, assigns them a product, processes their payments, and displays their account details.
