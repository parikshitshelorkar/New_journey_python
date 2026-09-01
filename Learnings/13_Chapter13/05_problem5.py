from functools import reduce
l = [1, 34, 2, 65, 635, 74, 45, 55]

def greater(a, b):
    if(a>b):
        return a
    return b
print(reduce(greater, l))
