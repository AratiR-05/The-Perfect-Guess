import random
randNumber = random.randint(1,100)
userGuess = None
Guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter Your Guess from 1 to 100 :"))
    Guesses +=1
    if(userGuess == randNumber):
        print("You Guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You Guessed it Wrong! Enter a smaller Number.")
        else:
            print("You Guessed it Wrong! Enter a greater Number.")   

print(f"You Guessed the Number in {Guesses} guesses")
with open("hiscore.txt","r")as f:
    hiscore = int(f.read())
if(Guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", 'w') as f:
        f.write(str(Guesses))                   