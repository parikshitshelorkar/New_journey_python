word = "Donkey"

with open("file1.txt") as f:
    content = f.read()

newcontent = content.replace(word, "###")

with open("file1.txt", "w") as f:
    f.write(newcontent)
