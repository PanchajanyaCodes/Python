# Problem 4
# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

word = "donkey"

with open("./text/donkey.txt") as file:
    content = file.read()

content_name = content.replace(word, "#####")

with open("./text/donkey.txt", "w") as file:
    file.write(content_name)
