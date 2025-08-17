'''
1=rock
0=paper
-1=scissors
'''
import random
value={"rock":1, "paper":0,"scissors":-1}
reverse_value={1:"rock", 0:"paper", -1:"scissors"}
choice=input("choose between \"rock\", \"paper\", and \"scissors\": ").lower()
num_value=(value[choice])
system=random.choice([1,0,-1])
print(f"system choose {reverse_value[system]} \nyou choose  {choice.capitalize()}")
if system==num_value:
    print("IT'S A DRAW!!")
else:
    if system==1 and num_value==0:
        print("YOU WIN !!")
    elif system==1 and num_value==-1:
        print("SYSTEM WON !!")
    elif system==0 and num_value==1:
        print("SYSTEM WON !!")
    elif system==0 and num_value==-1:
        print("YOU WON !!")
    elif system==-1 and num_value==0:
        print("SYSTEM WON !!")
    elif system==-1 and num_value==1:
        print("YOU WON !!")
    else:
        print("Something went wrong")