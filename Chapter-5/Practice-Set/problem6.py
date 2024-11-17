# Problem 6
# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dictionary = {}

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")
dictionary.update({name: lang})

name = input("\nEnter your name: ")
lang = input("Enter your favorite language: ")
dictionary.update({name: lang})

name = input("\nEnter your name: ")
lang = input("Enter your favorite language: ")
dictionary.update({name: lang})

name = input("\nEnter your name: ")
lang = input("Enter your favorite language: ")
dictionary.update({name: lang})

print("\n", dictionary)
