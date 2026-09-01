def divisible(n):
    if(n%5==0):
        return True
    return False

a = [2, 20, 350, 5, 444, 56, 38, 99]
f = list(filter(divisible, a))
print(f)