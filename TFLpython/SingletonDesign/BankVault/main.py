class BankVault():
    __instance = None

    def __new__(cls):

        if cls.__instance is None:
            print("Creating the vault...")
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.balance = 1000000

    def __str__(self):
        return f"The Balance is : {self.balance}"

vault1 = BankVault()
vault2 = BankVault()

print(vault1 is vault2)
print(vault1)

