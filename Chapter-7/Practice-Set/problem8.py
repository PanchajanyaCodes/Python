# Problem 8
# Write a program to print the following star pattern, for n = 3.
""" 
* 
** 
***
"""

n = 3

for i in range(1, n + 1):
    print("*" * (i * 2 - i))

# 1 * 2 - 1 = 1
# 2 * 2 - 2 = 2
# 3 * 2 - 3 = 3
