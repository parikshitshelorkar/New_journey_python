#self logic
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a>b):
    max = a
else: max = b
if(max<c):
    max = c
if(max<d):
    max = d


print(max)



#copilot used
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:
    max_val = a
else:
    max_val = b

if max_val < c:
    max_val = c

if max_val < d:
    max_val = d

print("The greatest integer is:", max_val)


#harrybhai's logic
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a>b and a>c and a>d):
    print("Greatest number is :", a)
elif(b>a and b>c and b>d):
    print("Greatest number is :",b)
elif(c>a and c>b and c>d):
    print("Greatest number is :",c)
elif(d>a and d>b and d>c):
    print("Greatest number is :",d)