#Write a  program using function to find whether the number entered by user is Even or odd. 
def oddeven(n):
    if n%2 == 0:
        return "Number is Even"
    else:
        return "Number is odd"
x = int(input("Enter any number: "))
print(oddeven(x))