from models.customer import Customer
from accounts.bank_account import BankAccount
from models.manager import Manager
from utils.file_handler import save_customers_to_csv

def main():
    customers = []

    c1 = Customer("madrid", "madrid@gmail.com", "C001")
    acc1 = BankAccount("Madrid")
    c1.add_account(acc1)
    acc1.deposit(2000)

    customers.append(c1)

    manager = Manager("Mr. John", "E001")
    print("\n--- Customer List ---")
    manager.view_all_customers(customers)

    print("\n--- Transaction Logs ---")
    manager.view_transaction_logs()

    save_customers_to_csv(customers)

if __name__ == "__main__":
    main()
