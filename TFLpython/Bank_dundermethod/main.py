import bank_account as ba

if __name__ == "__main__":
    # Code here only runs if you execute this file directly

    # Create a new account
    account1 = ba.BankAccount("Alice", 1000)
    account2 = ba.BankAccount("Parikshit", 50000)

    # Deposit and withdraw
    account1.deposit(500)
    account1.withdraw(300)

    account2.deposit(1000)
    account2.withdraw(60000)  # This should show insufficient balance

    # Print the object
    print(account1)
    print(account2)
     