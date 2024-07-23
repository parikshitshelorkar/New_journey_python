with open("log.html") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes, 'python' is present in the line number {lineno}")
        break
    lineno += 1
else:
    print("No there is no python in the file")
