def fibonacci():
    len = int(input("Enter the length of fibonacci series"))
    a = 0
    b = 1
    print(a, end=" ")
    print(b, end = " ")
    for i in range(len):
            c = a+b
            print(c, end=" ")
            a,b = b,c
fibonacci()   
