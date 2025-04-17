class Customer:
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display(self):
        print(f"Customer: {self.name}, Account Number: {self.account_number}, Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, account_number, initial_balance=0.0):
        if account_number in self.customers:
            print("Account number already exists")
        else:
            customer = Customer(name, account_number, initial_balance)
            self.customers[account_number] = customer
            print(f"Added new customer: {name}")

    def remove_customer(self, account_number):
        if account_number in self.customers:
            del self.customers[account_number]
            print(f"Removed customer with account number: {account_number}")
        else:
            print("Customer not found")

    def get_customer(self, account_number):
        return self.customers.get(account_number, None)

    def display_all_customers(self):
        for customer in self.customers.values():
            customer.display()
