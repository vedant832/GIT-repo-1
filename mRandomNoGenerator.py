


def talk(text):
    engine.say(text)
    engine.runAndWait()

print("---------------------------------------")
print("WELOCME TO THE GAME OF PERFECT GUESS")
print("---------------------------------------")
print("\n")
print("\n")
print("=======================================")
print("\t\tLEVELS\t\t")
print("1.EASY")
print("2.MEDIUM")
print("3.HARD")
print("=======================================")
levelchoice= int(input("CHOOSE LEVEL : \n"))
if(levelchoice==1):
   Compchoice=random.randint(1,10)
   talk("Your range of deduction lies between 1 to 10")
elif(levelchoice==2):
    talk("Your range of deduction lies between 1 to 50 ")
    Compchoice=random.randint(1,50)
elif(levelchoice==3):
    Compchoice=random.randint(1,100)
    talk("Your Range of deduction lies between 1 to 100")
else:
    print("INVALID CHOICE!")
    talk("YOU SHOULD MAKE CHOICE BETWEEN THE 3 levels above ")
    levelchoice= int(input("CHOOSE LEVEL : \n"))

playerchoice=None
guesses=0

while(playerchoice!=Compchoice):
    playerchoice=int(input("Give a choice to me : "))
    talk("REMEMBER YOUR RANGE")
    guesses=guesses+1
    if(playerchoice==Compchoice):
        print("You got it right!")
        talk("MAN ! YOU GOT SOME SPRIT")
    else:
        if(playerchoice<Compchoice):
            print("GUESS HIGH ! ")
        else:
            print("NOT THIS MUCH HIGH !")
    if(guesses==5):
        talk("WANT A HINT ?")
        wish=input("Y/N : \n")
        if(wish=="Y" and Compchoice%2==0 and playerchoice!=Compchoice  ):
            print("The number is even")
        else:
            print("the Number is odd")

        if (Compchoice-5==0):
            print("One of the next 5 digits is your answer")
        else:
            print("we dont have any hints")

    else:
        pass
print(f"YOU MADE IT IN {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
