# Open the file in write mode ("w")
with open("hellow.txt", "w") as file:
    file.write("This is the new content of the file.\n")
    file.write("Previous content is deleted.")
    
    file=open("hellow.txt","r")
    content=file.read()

print(content)
file.close()