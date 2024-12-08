# Problem 8
# Write a python function to print multiplication table of a given number.

def print_table(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number*i}")


number = int(input("Enter a number: "))
print_table(number)
