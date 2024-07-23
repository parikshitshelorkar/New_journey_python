import random
computer = random.choice([1, 0, -1])

Dict ={"s":1, "w":-1, "g":0}
revDict ={1:"Snake", -1:"Water", 0:"Gun"}
youstr = input("Enter your choice (|Snake-s| |water-w| |gun-g|) :")
you = Dict[youstr]
print(f"You choosed {revDict[you]}\nComputer choosed {revDict[computer]}")

if(computer==you):
    print("It's a Draw!")
else:
    if(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You win!")
    elif(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==0 and you==1):
        print("You lose!")
    elif(computer==0 and you==-1):
        print("You win!")
        '''
s=1
w=-1
g=0

'''