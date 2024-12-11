text = "Hello World!, I am here to learn Python Programming."

# Opening the file.
file = open("./text/file2.txt", "w")

# Writing to the file.
file.write(text)

# Closing the file.
file.close()

# NOTE: If the file is not present in the current directory, then a new file with the specified name will be created and given text is added to it.
