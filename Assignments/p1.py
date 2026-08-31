#) Write a program to check whether a given string starts with specified character    
str = input("Enter a string: ")
char = input("Enter a character: ")
if str.startswith(char):
    print("The string starts with the specified character.")
else:
    print("The string does not start with the specified character.")      
