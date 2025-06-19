from models.person import Person
from accounts.bank_account import BankAccount

class Customer(Person):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account: BankAccount):
        self.accounts.append(account)

    def __str__(self):
        return f"Customer {self.customer_id}: {super().__str__()}"
