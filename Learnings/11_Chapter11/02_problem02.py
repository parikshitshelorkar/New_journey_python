class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("Doggy don..!!")

# d = Dog()
# d.bark()

Dog.bark()