# Problem 7
# Write a program to print the following star pattern for n = 3.
"""
*
*** 
*****   
"""

n = 3
for i in range(1, n + 1):
    print('*' * (2 * i - 1))


# 1 * 2 - 1 = 1
# 2 * 2 - 1 = 3
# 3 * 2 - 1 = 5
