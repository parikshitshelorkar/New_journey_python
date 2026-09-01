import os
f = open("poem.txt", "r")
txt = f.read()
if "twinkle" in txt:
        print("Twinkle is present in the file")
else:
        print("Twinkle is not present in the file")
f.close()

