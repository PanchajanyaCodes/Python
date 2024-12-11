# Problem 11
# Write a python program to rename a file to “renamed_by_python.txt.

import os


with open("./text/rename.txt") as file:
    content = file.read()

with open("./text/renamed_by_python.txt", "w") as file:
    file.write(content)

# Delete the file
os.remove("./text/rename.txt")
