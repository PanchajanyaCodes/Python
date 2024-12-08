# Problem 4
# Write a recursive function to calculate the sum of first n natural numbers.


def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n-1)


number = int(input("Enter a positive integer: "))

result = sum_of_natural_numbers(number)
print(f"The sum of the first {number} natural numbers is {result}")
