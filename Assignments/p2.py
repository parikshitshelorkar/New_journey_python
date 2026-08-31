#Write a program using function to find greatest of three numbers by passing number as arguments

def greatest(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        gr = num1
    elif (num2 > num1 and num2 > num3):
        gr = num2
    elif (num3 > num1 and num3 > num2):
        gr = num3
    else:
        gr = num1
    return gr
        
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("The greatest number is:", greatest(a, b, c))