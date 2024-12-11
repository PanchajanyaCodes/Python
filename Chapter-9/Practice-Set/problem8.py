# Problem 8
# Write a program to make a copy of a text file “this.txt”

with open("./text/this.txt") as file:
    content = file.read()

with open("./text/this2.txt", "w") as file:
    file.write(content)
