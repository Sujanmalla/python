class employ :
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)
        print(f"New Salary after 20% increase: {self.salary}")


emp1 = employ("A", 30, 50000)
emp2 = employ("B", 25, 60000)


print("Employee 1 details:")
emp1.display()
emp1.increase_salary(20)

print("\nEmployee 2 details:")
emp2.display()
emp2.increase_salary(20)