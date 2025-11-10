import csv

fields = ["Name", "Subject", "Marks"]


rows = [
    ["Alice", "Math", 85],
    ["Bob", "Science", 90],
    ["Charlie", "English", 60],
    ["David", "Computer", 92],
    ["Eva", "History", 55]
]


with open("students.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)       
    csvwriter.writerows(rows)       

print("✅ students.csv file created successfully.") 
