# Problem 7
# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Type something: ").lower()

if "harry" in post:
    print("This post is talking about Harry.")
else:
    print("This post is not related to Harry.")
