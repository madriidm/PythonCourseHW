from .account import BankAccount
from .transaction import TransactionLog

class BankSystem:
    def __init__(self):
        self.accounts = []
        self.logs = {}

    def add_account(self, account):
        self.accounts.append(account)
        self.logs[account.account_number] = TransactionLog()

    def show_all_accounts(self):
        for account in self.accounts:
            print(account)

    def find_account_by_number(self, number):
        for account in self.accounts:
            if account.account_number == number:
                return account
        return None

    def log_transaction(self, account_number, transaction):
        if account_number in self.logs:
            self.logs[account_number].record(transaction)
