# Snake Water Gun Game : created by Sagar Yadav 
"""Run it on PC for best results
You have to enter two values-round and choice
You will get a csv file named "Snake Water Gun Game Winner.csv",after game ends."""

print("""
-------------------------How to play?-------------------------------
 Enter how many rounds you want to play in integer values?
 Enter your choices-
 For Snake - s
 For Water - w
 For Gun - g
 Enter your choice: s or w or g
---------------------------------------------------------------------""")

# Created by Sagar yadav
print("Snake Water Gun Game : Created by Sagar yadav")

import random

# Snake Water Gun Game : created by Sagar Yadav 
def gameWin(comp, you):
    global result
    # If two values are equal, declare a tie!
    if comp == you:
        result="Tie!"
        return result

    # Check for all possibilities when computer chose s
    elif comp == 'Snake':
        if you=='Water':
            result="Lose!"
            return result
        elif you=='Gun':
            result="Win!"
            return result
    
    # Check for all possibilities when computer chose w
    elif comp == 'Water':
        if you=='Gun':
            result="Lose!"
            return result
        elif you=='Snake':
            result="Win!"
            return result
    
    # Check for all possibilities when computer chose g
    elif comp == 'Gun':
        if you=='Snake':
            result="Lose!"
            return result
        elif you=='Water':
            result="Win!"
            return result
            
#Importing csv to collect the data of game
import csv
# Writing the csv file to store the data of the game
gWin = open("Snake Water Gun Game Winner.csv","w", newline = "")
gwinner = csv.writer(gWin)
#Program by Sagar Yadav
gwinner.writerow(["ROUND","COMPUTER CHOSE","YOU CHOSE","RESULT"])

rounds =  int(input("Enter how many rounds do you want to play? : "))

WinRounds=[]  #ROUNDS WHICH YOU WIN
LoseRounds=[] #Rounds which you lost
TieRounds=[]  #Rounds which ties
    
for time in range(rounds) :
    print()
    Round = time + 1
    print("Round -: ",Round)
    print("Computer's turn and he has already chosen his weapon\step")
    randNo = random.randint(1, 3) 
    if randNo == 1:
        comp = 'Snake'
        
        
    elif randNo == 2:
        comp = 'Water'
       
        
    elif randNo == 3:
        comp = 'Gun'
       
    you = input("Your Turn: Snake(s) Water(w) or Gun(g)? : ")
 #Program by Shiva   
    if you=="s" or you=="S":
        you="Snake"
    elif you=="w" or you=="W":
        you="Water"
    elif you=="g" or you=="G":
        you="Gun"
    else:
        print("You entered : ",you)
        print("You entered a wrong keyword >>> Game closing...")
        break
                                                                            # Created by Sagar Yadav
    a = gameWin(comp, you)

    print("Computer chose : ",comp)
    print("You chose : ",you)

    print("Result :~ ",result)

    if result=="Win!":
        WinRounds.append(Round)
    elif result=="Lose!":
        LoseRounds.append(Round)
    elif result=="Tie!":
        TieRounds.append(Round)
    else:
        pass
 #Program by Sagar Yadav
    records = [Round,comp,you,result]
    gwinner.writerow(records)
gWin.close()

# Reading the csv file to get result of the game
with open("Snake Water Gun Game Winner.csv","r+") as gWinRead:
    greader = csv.reader(gWinRead)
    wcount = 0                          #win count
    lcount=0                            #lose count
    tcount = 0                          #tie count
    
    for win in greader:
        if "Win!" in win :
            wcount += 1
        elif "Lose!" in win :
            lcount += 1
        elif "Tie!" in win :
            tcount += 1
    print(55 * "*")
    print("\t~Rounds Result~")
    print("Round(s)-------")
    if wcount >=1:
        print("You won :", wcount, "round(s) \n\t Rounds which you Won are :- ",WinRounds)
    if lcount >=1:
        print("You lost :", lcount, "round(s) \n\t Rounds which you Lost are :- ",LoseRounds)
    if  tcount >=1:
        print("The Game ties :", tcount, "round(s) \n\tRounds which Ties are :- ",TieRounds)
    print(55 * "+")
    print("\n\t\t`````````````````END RESULT``````````````````")
    if wcount > lcount:
        print("You Won the game..........")
    elif wcount < lcount:
        print("You lost the game.........")
    elif wcount == lcount:
        print("The Game ties,no one win or lost.........")
    print(55 * "*")


print()
print(">>>>>>>>>>>>>>>>>> GAME OVER <<<<<<<<<<<<<<<<<<<<<")
print("THANKS FOR PLAYING!")
print('\nCreated by Sagar Yadav')
#Program by Sagar Yadav

