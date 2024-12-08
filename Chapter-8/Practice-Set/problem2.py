# Problem 2
# Write a python program using function to convert Celsius to Fahrenheit.

def convert_to_fahrenheit(celsius):
    temperature = (celsius*(9/5))+32
    return temperature


celsius = float(input("Enter Celsius: "))

fahrenheit = convert_to_fahrenheit(celsius)
print(fahrenheit)
