class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} to account {self.account_number}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}")
        else:
            print("Insufficient balance or invalid amount.")

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance: ${self.balance})"
