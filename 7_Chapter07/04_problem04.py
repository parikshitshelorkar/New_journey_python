n = int(input("Enter the Number : "))
for i in range(2, n):
    if(n%i == 0):
        print("This is not a prime number!")
        break

else:
    print("This is a prime number!")
