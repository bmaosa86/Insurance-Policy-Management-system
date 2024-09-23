class Payment:
    def __init__(self, amount, policyholder):
        self.amount = amount
        self.policyholder = policyholder
        self.status = "pending"
        self.penalty = 0

    def process_payment(self):
        self.status = "completed"
        self.policyholder.payment_status[self.policyholder.name] = "Paid"
        print(f"Payment of {self.amount} processed for {self.policyholder.name}.")

    def send_reminder(self):
        if self.status == "pending":
            print(f"Reminder: Payment of {self.amount} is due for {self.policyholder.name}.")

    def apply_penalty(self):
        if self.status == "pending":
            self.penalty = self.amount * 0.1
            print(f"Penalty of {self.penalty} applied to {self.policyholder.name} for late payment.")
