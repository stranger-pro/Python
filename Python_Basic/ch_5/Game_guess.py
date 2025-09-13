import random

def guess(num,player,count=0):
    if(count==0):
        print(f"Game Start Player {player} ...")
    user = int(input("Guess The Number Between 1 to 100 : "))
    if(user==num):
        print("Correct Guess !")
        return (count + 1) 
    elif(user<num):
        print("Higher Number Please :")
        return guess(num,player,count+1)
    else:
        print("Lower Number Please :")
        return guess(num,player,count+1)

def Start():
    num1 = random.randint(1,100)
    a = guess(num1,"A")
    num2 = random.randint(1,100)
    b = guess(num2,"B")
    

    if(a==b):
        return f"Tie : Score = {a} and {b}"
    elif(a>b):
        return f"Player B is Winner : Score = {a} and {b}"
    else:
        return f"Player A is Winner : Score = {a} and {b}"

Game = Start()

print(Game)