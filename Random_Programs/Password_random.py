import random
chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,./?><MNBVCXZ:LKJHGFDSAPOIUYTREWQ!@#$%^&*()_+=-0987654321"
length = int(input("Enter length : "))
password = "" 
for a in range(length):
    password +=random.choice(chars)
print(password)
