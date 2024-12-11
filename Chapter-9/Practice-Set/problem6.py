# Problem 6
# Write a program to mine a log file and find out whether it contains ‘python’.

with open("./text/temp.log") as file:
    content = file.read()

    if "python" in content:
        print("python is present.")
    else:
        print("python is not present.")
