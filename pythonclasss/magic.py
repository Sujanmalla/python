class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee("Lemon", 50000)
print(emp.name)   


#_init_(self,...)  called authomatically when you create an object. it initializes attributes 
