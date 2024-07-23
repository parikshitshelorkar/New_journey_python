import random

def game():
    print("Your are playing the game")
    score = random.randint(1, 55)
    #fetching hiscore
    with open("hiscore.txt", "r") as h:
        hiscore = h.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

        print(f"Your score is {score}")

        if score>hiscore:
            with open("hiscore.txt", "w") as h:
                h.write(str(score))

    return score
game()