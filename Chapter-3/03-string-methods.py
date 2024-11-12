# String Functions.

topic = "python programming"

# 'len' function is used to find length of the string.
print(len(topic))  # 6

# 'endswith' method checks if the string ends with the given substring.
print(topic.endswith("on"))  # True

# 'startswith' method checks if the string starts with the given substring.
print(topic.startswith("yt"))  # False

# capitalize() method makes the first letter uppercase.
print(topic.capitalize())  # Python

# 'lower' method is used to convert the string into lowercase.
print(topic.lower())  # python

# 'upper' method is used to convert the string into uppercase.
print(topic.upper())  # PYTHON

# title() method makes the first letter of each word uppercase.
print(topic.title())  # Python

# find() method determines the index of the first occurrence of the given substring in a string.
print(topic.find("pro"))  # 7

# replace() method replace all occurrences of the given substring in a string.
print(topic.replace("p", "P"))

# splits() the string into a list of separate substrings based on the specified separator.
print(topic.split(" "))  # ["python", "programming"]

# count() method determines the count of specified substring in a string.
print(topic.count("p"))  # 2

# join() method join elements of an iterables into a string with each element separated by the string..
itr = ["Coder", "Coder"]
print(" - ".join(itr))  # Coder - Coder

# strip() method remove trailing whitespaces from the string.
new_str = "     Hello World!     "
print(new_str.strip())  # 'Hello World!'

# 'lstrip' method removes the whitespaces from the left side.
print(new_str.lstrip())  # 'Hello World!      '

# 'rstrip' method removes the whitespaces from the right side.
print(new_str.rstrip())  # '      Hello World!'

# 'isdigit' method check if all character of a string are digits.
this_str = "567"
print(this_str.isdigit())  # True

# 'isalpha' method checks if all characters of a string are alphabets.
that_str = "Programming"
print(that_str.isalpha())  # True

# 'isalnum' method checks if all characters of a string are alphabets and numbers.
new_str = "Code11"
print(new_str.isalnum())  # True

# 'swapcase' method swaps the case of the string.
print(that_str.swapcase())  # pROGRAMMING

# 'zfill' method pads a numeric string on left with 0 to fill a given width.
a = '1'
print(a.zfill(5))  # 00001
