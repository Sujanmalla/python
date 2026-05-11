
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

emp = Employee("Lemon", 50000)
print(emp)   

#str__ (self) Define what print(object) shosws