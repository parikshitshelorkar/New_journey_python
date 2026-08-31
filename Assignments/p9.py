#Write a program to create a class should with the attribute name, roll no, & age & display data of 4 students.
class Student():
    def __init__(self, name, rollno, age):
        self.name = name
        self.rollno = rollno
        self.age = age
        pass
    def  display(self):
        print("Student Name :", self.name)
        print("Roll No.     :", self.rollno)
        print("Age          :", self.age)
#creation of four objects
obj1 = Student("Parikshit", "13C1452", 18)
obj2 = Student("Aarav", "13C1453", 19)
obj3 = Student("Ishita", "13C1454", 18)
obj4 = Student("Riya", "13C1455", 20)
#calling display function
obj1.display()
obj2.display()
obj3.display()
obj4.display()
