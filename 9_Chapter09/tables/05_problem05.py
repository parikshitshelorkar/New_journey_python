words = [ "gadha", "duffer", "nalayak", "harami", "mc", "bc", "land" ]

with open("file1.txt") as f:
    content = f.read()

    for word in words:
        content = content.replace(word, "#"*len(word))

with open("file1.txt", "w") as f:
    f.write(content)  
