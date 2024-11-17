# Problem 5
# Write a program which finds out whether a given name is present in a list or not.

name_list = ["mike", "peter", "natasha", "emma", "alexa", "ruskin"]

name = input("Enter a name: ").lower()

if name in name_list:
    print(f"{name} is invited in the party.")
else:
    print("Sorry! you are not invited.")
