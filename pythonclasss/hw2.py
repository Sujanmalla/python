import csv


students = [
    ["Alice", "Math", 85],
    ["Bob", "Science", 90],
    ["Charlie", "English", 60],
    ["David", "Computer", 92],
    ["Eva", "History", 55]
]

fields = ["Name", "Subject", "Marks"]

with open("students_marks.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)       
    writer.writerows(students)  

print("students_marks.csv created successfully!")


with open("students_marks.csv", 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  
    filtered = [row for row in reader if int(row[2]) > 60]


with open("students_above_60.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)       
    writer.writerows(filtered)    

print("students_above_60.csv created successfully (marks > 60)!")





