# Problem 1
# Write a program using functions to find greatest of three numbers.

def find_greatest(a, b, c):
    if a > b and a > c:
        return f"{a} is greater."
    elif b > a and b > c:
        return f"{b} is greater."
    elif c > a and c > b:
        return f"{c} is greater."
    else:
        return "All are equal."


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

result = find_greatest(n1, n2, n3)
print(result)
