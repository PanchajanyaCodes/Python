# Problem 3
# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 - year old.

def generate_multiplication_table(number, folder_path):
    """Generate multiplication table for a given number and write it to a file."""
    file_path = f"{folder_path}/{number}_table.txt"

    with open(file_path, "w") as file:
        for i in range(1, 11):
            file.write(f"{number} x {i} = {number * i}\n")


def main():
    """Generate and save multiplication tables from 2 to 20 in individual files."""
    folder_path = "Tables"

    for number in range(2, 21):
        generate_multiplication_table(number, folder_path)

    print(f"Multiplication tables from 2 to 20 have been generated and saved in the '{
          folder_path}' folder.")


main()
