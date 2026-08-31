#Write a program to calculate area of triangle using a class
class Area:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        a = 0.5*self.base*self.height
        print("Area is: ", a)

#Taking input lengt and breadth
l = int(input("Enter lenght: "))
b = int(input("Eneter breadth : "))
#Callin functionns
triangle = Area(l, b)
triangle.area()