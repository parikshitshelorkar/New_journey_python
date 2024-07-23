def pattern(n):
    if(n==0):
        return
    print("*"*n)
    print(pattern(n-1))


print(pattern(3))