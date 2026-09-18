class BankAccount:
    # __init__ is called when a new account is created
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"Account for {self.name} created with balance {self.balance}")

    # __str__ is called when we print the object
    def __str__(self):
        return f"BankAccount({self.name}, Balance: ${self.balance})"

    # Example of adding money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    # Example of withdrawing money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance!")

            