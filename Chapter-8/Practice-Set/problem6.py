# Problem 6
# Write a python function which converts inches to cms.

def inches_to_centimeter(inches):
    centimeters = inches*2.54
    return (f"Centimeters: {centimeters}")


inches = int(input("Enter inches: "))

centimeters = inches_to_centimeter(inches)
print(centimeters)
