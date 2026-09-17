from Bank_dundermethod.BankAccount import BankAccount as ba
# Create a new account
account1 = ba("Alice", 1000)

# Deposit and withdraw
account1.deposit(500)
account1.withdraw(300)

# Print the object
print(account1)