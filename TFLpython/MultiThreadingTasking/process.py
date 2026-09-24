from multiprocessing import Process

def calculate():
    total = 0

    for i in range(10_000_000):
        total += i

    print(total)

p1 = Process(target=calculate)
p2 = Process(target=calculate)

p1.start()
p2.start()

p1.join()
p2.join()

print("Completed")