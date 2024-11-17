# Problem 2
# Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set()

n1 = int(input("Enter a number : "))
n2 = int(input("Enter a number : "))
n3 = int(input("Enter a number : "))
n4 = int(input("Enter a number : "))
n5 = int(input("Enter a number : "))
n6 = int(input("Enter a number : "))
n7 = int(input("Enter a number : "))
n8 = int(input("Enter a number : "))

s.update([n1, n2, n3, n4, n5, n6, n7, n8])
print(s)
