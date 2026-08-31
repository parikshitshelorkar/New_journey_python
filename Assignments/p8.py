# Write a program to display current directory, create a directory & remove the created directory

import os

# Display the current directory
current_directory = os.getcwd()
print("Current directory is:", current_directory)

# Create a new directory
new_directory = "newdr"
if not os.path.exists(new_directory):  # Check if the directory already exists
    os.mkdir(new_directory)
    print("New directory created:", new_directory)
else:
    print("Directory already exists:", new_directory)

# Remove the created directory
if os.path.exists(new_directory):  # Check if the directory exists before removing
    os.rmdir(new_directory)
    print("Directory removed:", new_directory)
else:
    print("Directory does not exist, cannot remove:", new_directory)
