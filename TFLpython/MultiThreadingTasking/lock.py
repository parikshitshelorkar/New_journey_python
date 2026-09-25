import threading

lock = threading.Lock()

balance = 1000

def withdraw(amount):
    global balance

    with lock:
        if balance >= amount:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")