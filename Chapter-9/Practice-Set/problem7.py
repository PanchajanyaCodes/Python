# Problem 7
# Write a program to find out the line number where python is present from ques 6.

with open("./text/temp2.log") as file:
    lines = file.readlines()

line_number = 1

for line in lines:
    if "python" in line:
        print(f"python is present in line {line_number}.")
        line_number += 1
