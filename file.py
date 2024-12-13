# Writing to a File

with open("example.txt", "w") as file:
    file.write("Hello, file!")

#reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
