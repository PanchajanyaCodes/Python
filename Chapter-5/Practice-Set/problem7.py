# Problem 7
# If the names of 2 friends are same; what will happen to the program in problem 6?

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

# The value of second friend will be considered as the value for the first friend.
