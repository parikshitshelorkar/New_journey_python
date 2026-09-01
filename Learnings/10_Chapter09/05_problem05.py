from random import randint


class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"The ticket is booked for train number {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"The train {self.trainNo} is running on time " )
    def getFare(self, fro, to):
        print(f"The ticket Fare for train {self.trainNo} from {fro} to {to} is {randint(222, 555)}")

t = Train(2444893)
t.book("Murtizapur", "Pune")
t.getStatus()
t.getFare("Murtizapur", "Pune")
