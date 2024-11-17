# Problem 1
# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

dictionary = {
    "bandar": "Monkey",
    "pani": "Water",
    "chai": "Tea",
    "dudh": "Milk",
    "kutta": "Dog"
}

user_input = input(
    "Enter a word to search its meaning (bandar, pani, chai, dudh, kutta): ")
print(dictionary[user_input])
