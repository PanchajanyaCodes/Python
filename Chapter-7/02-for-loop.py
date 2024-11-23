# For Loop.
for i in range(1, 11):
    print(i)
print("\n")

# Else with For Loop.
items = ["shampoo", "cabbage", "biscuits", "chips", "pineapple", "butter"]
for i in range(len(items)):
    print(items[i])
else:
    print("Out of the loop.")
print("\n")

# Break Statement.
# Instructs the program to exit the loop.
for i in range(1, 6):
    if i == 4:
        break
    else:
        print(i)  # 1 2 3
print("\n")

# Continue Statement.
# Used to stop the current iteration and continue with another iteration.
for i in range(1, 6):
    if i == 4:
        continue
    else:
        print(i)  # 1 2 3 5
print("\n")

# Pass Statement.
# It instructs to do nothing.
for i in range(1, 11):
    pass
