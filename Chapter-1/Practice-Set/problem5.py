# Problem 5
# Label the program written in problem 4 with comments.

# Import the os module to interact with the operating system.
import os

# Specify the relative path to the directory.
directory_path = '../Practice-Set'

# Check if the specified path is a directory.
if os.path.isdir(directory_path):
    # If it is a directory, get the list of all files and directories within it.
    contents = os.listdir(directory_path)
    # Iterate over the list of contents and print each item.
    for item in contents:
        print(item)
else:
    # If the specified path is not a directory, print an error message.
    print(f"The path {directory_path} is not a directory.")
