p = int(input("Enter your physics marks :"))
c = int(input("Enter your chemistry marks :"))
m = int(input("Enter your maths marks :"))

if(p>33 and c>33 and m>33):
    total_percentage = (p + c + m)*100/300

    if(total_percentage>=40):
        print("You are passed the Exam with",total_percentage,"%")
    else: print("You are failed..")

else: print("Your subject grouping is not clear!!\nyou are failed")
        
