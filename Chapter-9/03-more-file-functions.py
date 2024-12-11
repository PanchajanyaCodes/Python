# Opening the file.
file = open("./text/file3.txt")

# Reading each line from the file.
lines = file.readlines()

"""
# Read line one by one.
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
"""

# Printing all lines in a list.
print(lines, type(lines))


"""
# Printing lines one by one.
print(line1)
print(line2)
print(line3)
"""

# Closing the file.
file.close()


# NOTE: 'readlines()' method returns a list of the lines present in the file.
