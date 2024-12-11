# Problem 5
# Repeat program 4 for a list of such words to be censored.

words = ["donkey", "pig", "asshole"]

with open("./text/donkey2.txt") as file:
    content = file.read()


for word in words:
    content = content.replace(word, "#"*len(word))

with open("./text/donkey2.txt", "w") as file:
    file.write(content)
