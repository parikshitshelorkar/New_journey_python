from concurrent.futures import ProcessPoolExecutor

def calculate(n):
    return n*n

numbers = [10, 20, 30, 40]

with ProcessPoolExecutor() as executor:
    results = executor.map(calculate, numbers)

print(list(results))
