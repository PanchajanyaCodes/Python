# Problem 5
# Write a python function to print first n lines of the following pattern:  for n = 3
""" 
*** 
**                
* 
"""


def print_pattern(n=3):
    for i in range(3, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


print_pattern()
