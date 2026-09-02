#this project is created by an inspiration of anshuman!
#which calculates compound interest

p =int(input("Enter the amount : "))
r = float(input("Enter the rate : "))
n = 1+r
t = int(input("Enter the time period : "))

f = (n)**t
fin = p*f

print(f"The final amount will be {fin}")

'''
    (p*1.1)**5
    
'''
    
    