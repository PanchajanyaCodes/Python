# Making Tuple.
empty_tuple = ()
single_element_tuple = ("one",)
mr_tuple = ("one", "two", 3)

print(empty_tuple)
print(type(empty_tuple))

print(single_element_tuple)
print(type(single_element_tuple))

print(mr_tuple)
print(type(mr_tuple))

# Accessing tuple element.
print(mr_tuple[0])

# Tuple slicing.
print(mr_tuple[1: 3])

# Tuple concatenation.
print(single_element_tuple + mr_tuple)

# Unpacking tuple.
a, b, c = mr_tuple
print(a, b, c)

# 'len' function is used to determine length of the tuple.
print(len(mr_tuple))  # 3

# 'count' method returns the number of occurrence of specified elements in the tuple.
print(mr_tuple.count("one"))  # 1

# 'index' method returns the index of first occurrence of a specified element.
print(mr_tuple.index("one"))  # 0
