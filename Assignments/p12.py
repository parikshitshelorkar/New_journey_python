# Write a program to create a class employee with the attribute name, emp-id & Salary  & display data of 2 employees.
class Employee():
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name   :", self.name)
        print("Emp-id :", self.emp_id)
        print("Salary :", self.salary)
        print("")

#creating objects
e1 = Employee("Rushabh",  4593, 500000)
e2 = Employee("Sumit", 4890, 70000)
#calling display function
e1.display()
e2.display()