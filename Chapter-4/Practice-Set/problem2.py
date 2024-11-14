# Problem 2
# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

mark1 = int(input("Enter english marks: "))
marks.append(mark1)

mark2 = int(input("Enter math marks: "))
marks.append(mark2)

mark3 = int(input("Enter science marks: "))
marks.append(mark3)

mark4 = int(input("Enter python marks: "))
marks.append(mark4)

mark5 = int(input("Enter geography name: "))
marks.append(mark5)

mark6 = int(input("Enter french name: "))
marks.append(mark6)

marks.sort()
print(f"Marks: {marks}")
