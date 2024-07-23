#using while loop
n = int(input("Enter the Number : "))
# i = 1
# s = 1
# while(i<=n):
#     s = s*i
#     i += 1
# print("Factorial is :", s)

#using for loop
s = 1
for i in range(1, n+1):
    s = s*i
print(f"The factorial of {n} is {s}")
