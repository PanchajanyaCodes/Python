# Making List.
friends = ["bruce", "tony", "peter", "steve"]
print(friends)

# Accessing list element.
print(friends[0])

# List Slicing.
print(list[1:3])

# Re-assigning value to list element.
friends[3] = "natasha"
print(friends)

# List unpacking.
a, b, c, d = friends
print(a, b, c, d)

# 'len' function is used to determine length of the list.
print(len(friends))

# 'append' methods add element to the end of the list.
friends.append("thor")
print(friends)

# 'extend' method appends list from another list elements.
new_friends = ["bucky", "wanda"]
friends.extend(new_friends)
print(friends)

# 'insert' element to the specified position in the list.
friends.insert(7, "vision")
print(friends)

# 'remove' method remove first occurrence of the specified element.
friends.remove("vision")
print(friends)

# 'pop' method removes the last element from the list.
popped_item = friends.pop()
print(friends)
print(popped_item)  # "wanda"

# 'index' method returns the index of first occurrence of a specified element.
print(friends.index("natasha"))  # 3

# 'count' method returns the number of occurrence of specified elements in the list.
print(friends.count("steve"))  # 0

# 'sort' method returns the sorted list in ascending order.
friends.sort()
print(friends)

# 'reverse' method reverse the original list.
friends.reverse()
print(friends)

# 'copy' method returns a shallow copy of the original list.
friends_copy = friends.copy()
print(friends_copy)

# 'clear' method clears the entire list.
friends_copy.clear()
print(friends_copy)
