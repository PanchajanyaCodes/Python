# Problem 9
# Write a program to find out whether a file is identical & matches the content of another file.

with open("./text/file1.txt") as file:
    content1 = file.read()

with open("./text/file2.txt") as file:
    content2 = file.read()

if content1 == content2:
    print("Both files contains the same content.")
else:
    print("File content is not same.")
