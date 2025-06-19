from models.employee import Employee

class Manager(Employee):
    def view_all_customers(self, customers):
        for cust in customers:
            print(cust)

    def view_transaction_logs(self):
        try:
            file = open("data/transaction_log.txt", "r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No transactions found.")
