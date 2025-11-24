class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

emp1 = Employee("A", 50000)
emp2 = Employee("B", 60000) 

print(emp1 + emp2)   
