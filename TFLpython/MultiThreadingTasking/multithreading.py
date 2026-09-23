import threading
import time

def task1():
    print("Task 1 started")
    time.sleep(3)
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(3)
    print("Task 2 completed")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed")