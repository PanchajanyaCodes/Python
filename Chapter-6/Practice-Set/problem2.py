# Problem 2
# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter english marks: "))
sub2 = int(input("Enter computer marks: "))
sub3 = int(input("Enter maths marks: "))

marks_obtained = sub1+sub2+sub3
possible_marks = 300

total_percentage = (marks_obtained/possible_marks)*100
print(f"You scored {total_percentage}% marks.")

if total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("Yayy! you passed the exam.")
else:
    print("Oops! you failed the exam.")
