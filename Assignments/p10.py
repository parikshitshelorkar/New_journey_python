#Write a program that creates a class car with two attribute name & cost. Create two objects & display info.
class Car():
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        pass
    def displayinfo(self):
        print("Model Name: ", self.name)
        print("Cost      : ", self.cost)

obj1 = Car("TATA Nano", 100000)
obj2 = Car("MustangGT", 5000000)

obj1.displayinfo()
obj2.displayinfo()
