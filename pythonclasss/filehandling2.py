import os  

file_name = "example.txt"


with open(file_name, "w") as file:  
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")
print("File written successfully!")


with open(file_name, "r") as file:  
    content = file.read()
print("File content:")
print(content)

with open(file_name, "a") as file:  
    file.write("This line is added at the end.\n")
print("Line appended successfully!")


with open(file_name, "r") as file:
    content = file.read()
print("Updated File content:")
print(content)


if os.path.exists(file_name):
    os.remove(file_name)
    print(f"{file_name} has been deleted.")
else:
    print("File does not exist.")                



      






