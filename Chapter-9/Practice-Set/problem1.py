# Problem 1
# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("./text/poem.txt") as file:
    lines = file.read()

if "Twinkle" in lines:
    print("Twinkle is present in the file.")
else:
    print("Twinkle is not present in the file.")
