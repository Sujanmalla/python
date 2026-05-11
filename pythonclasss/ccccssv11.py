import csv

field = ['Name', 'Age', 'City']
rows = [
    ['Alice', 30, 'New York'], 
    ['Bob', 25, 'Los Angeles'], 
    ['Charlie', 35, 'Chicago']
]   
with open('people.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(rows)        


    in       