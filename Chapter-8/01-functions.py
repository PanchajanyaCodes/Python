# Making Function.
def greet():
    print("Hello Panchajanya!")


greet()  # Hello Panchajanya!


# Function with argument.
def greet(name):
    print(f"Hello {name}!")


greet("Panchajanya")  # Hello Panchajanya!


# Function with default argument.
def greet(name="Panchajanya"):
    return f"Hello {name}!"


msg = greet()
print(msg)  # Hello Panchajanya!

msg = greet("John Doe")  # Hello John Doe!
print(msg)  # Hello John Doe!
