class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

h = Programmer("Harry", 200000, 444107)
p = Programmer("Parikshit", 300000, 444107)
print(p.name, p.salary, p.pin)
print(h.name, h.salary, h.pin)
