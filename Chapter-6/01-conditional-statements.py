# Conditional Statements.
# if - elif - else.


age = int(input("Enter your age: "))

if age <= 0:
    print("Oh!, you don't even exist.")
elif age > 120:
    print("Sorry! but, Ghosts are not allowed here.")
elif age < 18:
    print("You are not mature enough to understand politics.")
else:
    print("We are glad you are here to vote.")
