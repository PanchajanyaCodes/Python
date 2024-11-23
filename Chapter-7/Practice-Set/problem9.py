# Problem 9
# Write a program to print the following star pattern. for n = 3
"""
* * * 
*   *     
* * * 
"""

n = 3

for i in range(n):
    for j in range(n):
        # Print '*' at the border
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()  # Move to the next line after each row
