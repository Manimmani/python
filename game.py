import random
import sys 
from enum import Enum
class RPS(Enum):
    ROCK = 1 
    PAPER = 2
    SCISSOR = 3
print("")
playerchoice=input("enter...\n1.ROCK \n2.PAPER \n3.SCISSOR\n\n")
player=int(playerchoice)
    
if (player < 1 or player > 3):
    sys.exit("must enter 1 , 2 or 3")
print("you chose : "+str(RPS(player)).replace("RPS.",""))
computerchoice=  random.choice("123")
computer=int(computerchoice)
print("python chose : "+str(RPS(computer)).replace("RPS.",""))
print("")
if player == 1 and computer == 3:
    print("🎉you win")
elif player == 2 and computer == 1:
    print("🎉you win")
elif player == 3 and computer == 2:
    print("🎉you win")
elif player == computer:
    print("😶tie game")
else:
    print("😒python win")

    

