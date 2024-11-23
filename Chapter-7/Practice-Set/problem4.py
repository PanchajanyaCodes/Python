# Problem 4
# Write a program to find whether a given number is prime or not.

number = int(input("Enter a number: "))

if number <= 1:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")