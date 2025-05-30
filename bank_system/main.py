from system.account import BankAccount
from system.bank_system import BankSystem

acc1 = BankAccount("001", "Alice", 1000)
acc2 = BankAccount("002", "Bob", 500)

bank = BankSystem()
bank.add_account(acc1)
bank.add_account(acc2)

acc1.deposit(200)
bank.log_transaction("001", "Deposit $200")

acc2.withdraw(100)
bank.log_transaction("002", "Withdraw $100")

bank.show_all_accounts()

print("\nTransaction log for account 001:")
print(bank.logs["001"])
