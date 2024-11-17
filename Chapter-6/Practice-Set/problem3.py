# Problem 3
# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

message = input("Enter your message: ").lower()

word1 = "make a lot of money"
word2 = "buy now"
word3 = "subscribe this"
word4 = "click this"

if word1 in message or word2 in message or word3 in message or word4 in message:
    print("Spam Detected!")
else:
    print("Safe Message.")
