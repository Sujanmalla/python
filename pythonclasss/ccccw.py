class employ :
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

   
def increase_salary(self, percent):
   
    increase = self.salary *  (percent / 100)
    new_salary = self.salary + increase
    self.salary = new_salary
    print("New Salary:", new_salary)
    return new_salary

     
emp1 = employ("A", 30, 50000)
emp2 = employ("B", 25, 60000)

print("Employee1 :")
emp1.display()
emp1.increase_salary(20)

print("\nEmployee2 :")
emp2.display() 
emp2.increase_salary(20) 