import time

def log_transaction(account_number, action, amount):
    now = time.strftime("%Y-%m-%d %H:%M:%S")

    with open("data/transaction_log.txt", "a") as file:
        line = now + " | " + account_number + " | " + action + " | $" + str(round(amount, 2)) + "\n"
        file.write(line)
