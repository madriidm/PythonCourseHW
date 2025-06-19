from transactions.transaction_logger import log_transaction

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        log_transaction(self.account_number, "DEPOSIT", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            log_transaction(self.account_number, "WITHDRAW", amount)
        else:
            print("Insufficient funds.")

    def __str__(self):
        return f"Account {self.account_number} | Balance: ${self.balance:.2f}"
