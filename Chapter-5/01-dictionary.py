# Making a dictionary.
person = {
    "name": "Vision",
    "age": 26,
    "city": "New York"
}

print(person)

# Accessing dictionary value.
print(person["name"])

# Adding key-value to a dictionary.
person["email"] = "vision0123@gmail.com"
print(person)

# Updating existing value of a dictionary.
person["age"] = 27
print(person)

# 'del' keyword is used to delete a key from the dictionary.
del person["email"]
print(person)

# 'pop' method is used to remove the specified element from the dictionary.
popped_item = person.pop("age")
print(person)
print(popped_item)

# 'keys' method returns a view object that displays a list of all the keys in the dictionary.
print(person.keys())

# 'items' method returns a view object that displays a list of dictionary's key-value tuple pairs.
print(person.items())

# 'popitem' method remove and return the last key-value pair from the dictionary.
popped_item = person.popitem()
print(person)
print(popped_item)

# 'values' method returns a view object that displays a list of all the values in the dictionary.
print(person.values())

# 'get' method returns the value for key if key is in the dictionary.
print(person.get("name"))

# 'copy' method returns a shallow copy of the original dictionary.
twins = person.copy()
print(twins)

# 'update' method updates the dictionary with the key-value pairs from another dictionary.
updates = {"age": 26, "email": "vision0123@gmail.com"}
person.update(updates)
print(person)

# 'fromkeys' method creates a new dictionary with the keys from the iterable and values all set to the specified value.
keys = ["country", "city", "house"]
values = "unknown"
new_dict = dict.fromkeys(keys, values)
print(new_dict)

# 'setdefault' method return the value if its key is present. If not then adds the key and set its value to the specified value.
new_person = {"name": "peter"}
age = new_person.setdefault("age", 25)
print(new_person)

print("Helo World!")
