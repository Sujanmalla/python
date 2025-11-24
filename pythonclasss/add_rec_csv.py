import csv

class Student:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll, age):
        self.students.append({"Name": name, "roll": roll, "age": age})

    def save_to_csv(self, filename):
        with open(filename, mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "roll", "age"])
            writer.writeheader()
            writer.writerows(self.students)

if __name__ == "__main__":
    s = Student()
    s.add_student("John", 101, 20)
    s.add_student("Alice", 102, 21)

    print(s.students)
    s.save_to_csv("students.csv")    
