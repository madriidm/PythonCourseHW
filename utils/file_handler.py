import csv
from models.customer import Customer
from accounts.bank_account import BankAccount

def load_customers_from_csv(file_path="data/customers.csv"):
    customers = []
    try:
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                customer = Customer(row["Name"], row["Email"], row["ID"])
                
                account_numbers = row["Accounts"].split(";")
                for acc_num in account_numbers:
                    if acc_num.strip():  
                        account = BankAccount(acc_num)
                        customer.add_account(account)

                customers.append(customer)

    except FileNotFoundError:
        print("No previous customer data found.")
    
    return customers
