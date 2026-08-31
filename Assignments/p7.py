#Write a python program that count number of tabs & new line character in a file. 

tabs = 0
new_lines = 0

# Open the file using a 'with' statement
with open("file.txt", "r") as f:
    for line in f:  # Read the file line by line
        tabs += line.count("\t")  # Count tabs in the current line
        new_lines += line.count("\n")  # Count new line characters in the current line

# Print the results
print("Number of tabs:", tabs)
print("Number of new line characters:", new_lines)
