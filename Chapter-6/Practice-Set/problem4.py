# Problem 4
# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your name: ")

if len(username) < 10:
    print("Your name contains less than 10 letters.")
else:
    print("Your name contains more than 10 letters.")
