#Write a program that copy content of one file into another file while copying all small letter should be converted to capital and vice versa.
f = open("file.txt", "r")
content = f.read()
f.close()

# Swap case of the content
swapped_content = content.swapcase()

# Write the swapped content to another file
g = open("cpy_file.txt", "w")
g.write(swapped_content)
print("Text copied...! ")