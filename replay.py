from time import sleep
import sys

import src.village as Base
import src.input as Input
import src.buildings as buildings
import src.walls as wall
import src.troops as troop

import os
import colorama
from colorama import Fore, Back, Style
MAX_BARBARIAN=20
Hspell=5
Rspell=5
colorama.init(autoreset=True)
Position1r = 24
Position1c = 15
Position2r = 34
Position2c = 135
Position3r = 14
Position3c = 135
kingCount = 1
game_over=0
percent=0
#Classes
call = Input.Get()
village=Base.Village()
Townhall = buildings.TownHall()
hut1 = buildings.Hut(10,30,18,50)
hut2 = buildings.Hut(30,30,38,50)
hut3 = buildings.Hut(10,100,18,120)
hut4 = buildings.Hut(30,100,38,120)
hut5 = buildings.Hut(6,65,14,85)
cannon1 = buildings.Cannon(20,35,28,50)
cannon2 = buildings.Cannon(20,105,28,120)
cannon3 = buildings.Cannon(31,70,39,85)
king = troop.King(Position2r,Position2c)
check=0

#arrays
walls=[]
Barbarians=[]
for i in range(MAX_BARBARIAN):
    Barbarians.append(troop.Barbs(Position1r,Position1c))


huts=[hut1,hut2,hut3,hut4,hut5]
cannons = [cannon1,cannon2, cannon3]
#variables
keyPress = ""
CurrentBarbCount =0 
CANVAS = [[Back.BLACK+" "] * village.WIDTH for _ in range(village.HEIGHT)]
colors =[Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.BLACK, Fore.CYAN]
count=0
for i in range(25,126):
    walls.append(wall.Wall(5,i))    
    walls.append(wall.Wall(40,i))
for i in range(6,40):
    walls.append(wall.Wall(i,25))
    walls.append(wall.Wall(i,125))

def FillCanvas():
    global CANVAS
    global game_over
    global percent
    village.buildCanvasFrame(CANVAS)
    village.addSpawnPoints(CANVAS)
    Townhall.AddTownhall(CANVAS)
    
    for i in range(5):
        huts[i].AddHut(CANVAS)
    
    
    
    for i in range(3):
        cannons[i].AddCannon(CANVAS)
        if(cannons[i].health>0):
            if(CurrentBarbCount>0 or kingCount==0):
                cannons[i].CannonFire(Barbarians,king)
            
    for wall in walls:
        wall.AddWall(CANVAS)
    c=0
    for i in range(MAX_BARBARIAN):
        if(Barbarians[i].existence==1):
            c=c+1
            tempClass = Barbarians[i].getTarget(huts,cannons,Townhall)
            Barbarians[i].update(tempClass,CANVAS,walls)
            Barbarians[i].display(CANVAS)
    # CurrentBarbCount = c
    if(kingCount==0):
        king.display(CANVAS)
    c=0
    for barb in Barbarians:
        if barb.health<=0:
            c=c+1
    if king.health<=0:
        c=c+1
    if c==21:
        game_over=1
    c=0
    percent=0
    for hut in huts:
        if hut.health<=0:
            c=c+1
            percent=percent+10
    for cannon in cannons:
        if cannon.health<=0:
            c=c+1
            percent=percent+5
    if Townhall.health<=0:
        c=c+1
        percent=percent+35
    if c==9:
        game_over=2    

    


def display():
    global CANVAS
    global count
    global keyPress
    if(game_over==0):
        print("    "*village.LEFT_PADDING+colors[count]+"  ---        ---          ---")
        print("    "*village.LEFT_PADDING+colors[count]+"/          /     \      /    ")
        print("    "*village.LEFT_PADDING+colors[count]+"\       .  \     /   .  \    ")
        print("    "*village.LEFT_PADDING+colors[count]+"  ---        ---          ---")
        string = []
        for i in range(0,7):
            string.append(' ')
        for i in range(0,7):
            if(king.health/3>=50 and king.health/3<=100 ):
                if(i<= 0+int(king.health/3*6/100)):
                    string[i]= Back.GREEN+' '
                else:
                    string[i]= Back.BLACK+' '
            if(king.health/3>=20 and king.health/3<50 ):
                if(i<= 0+int(king.health*6/300)):
                    string[i]= Back.YELLOW+' '
                else:
                    string[i]= Back.BLACK+' '
            if(king.health/3>0 and king.health/3<20 ):
                if(i<= 0+int(king.health/3*6/100)):
                    string[i]= Back.RED+' '
                else:
                    string[i]= Back.BLACK+' '
        print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"King's health:"+Back.BLUE+Fore.WHITE+str(" "+str(int(king.health/3))),end=" ")
        for i in range(7):
            print(string[i],end="")
        print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Used Barbarians:"+Back.BLUE+Fore.WHITE+str(" "+str(int(CurrentBarbCount))+" "),end="")
        print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Heal Spells : "+Back.BLUE+Fore.WHITE+str(" "+str(Hspell)+" "),end="")
        print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Rage Spells : "+Back.BLUE+Fore.WHITE+str(" "+str(Rspell)+" "))
        
        count=(count+1)%6
        print("\n".join(["".join(row) for row in CANVAS]), Style.RESET_ALL,end='')
        print()
    elif(game_over==1):
        print("D E F E A T")
        print("Percentage Destroyed : "+str(percent))
        # print("Press Enter for Replay")
        
    elif(game_over==2):
        print("V I C T O R Y")
        print("Percentage Destroyed : "+str(percent))
        # print("Press Enter for Replay")


    # print(keyPress)


os.system("stty -echo")
t=1

# replay feature
f = open(sys.argv[1], 'r')

while(keyPress != "q"):
    os.system("clear")
    if(game_over==0):
        FillCanvas()
    display()
    sleep(0.2)
    # if(game_over==0):
    temp=""
    keyPress=""
    while(temp!='@'):
        temp= f.read(1)
        if(temp!='@'):
            keyPress+=temp
    # print(keyPress)
    if(keyPress=="King1" and kingCount==1):
        king.r=Position1r
        king.c=Position1c
        kingCount=0
    if(keyPress=="King2" and kingCount==1):
        king.r=Position2r
        king.c=Position2c
        kingCount=0
    if(keyPress=="King3" and kingCount==1):
        king.r=Position3r
        king.c=Position3c
        kingCount=0    
    if(keyPress == "left" or keyPress == "right" or keyPress == "up" or keyPress=="down" and kingCount==0):
        king.update(keyPress,CANVAS)
    if(keyPress == "attack"):
        king.attack(huts, Townhall, walls, cannons)
    if(keyPress=="Barb1" and CurrentBarbCount<MAX_BARBARIAN):
        Barbarians[CurrentBarbCount].r=Position1r
        Barbarians[CurrentBarbCount].c=Position1c
        Barbarians[CurrentBarbCount].existence=1
        CurrentBarbCount=CurrentBarbCount+1
    if(keyPress=="Barb2" and CurrentBarbCount<MAX_BARBARIAN ):
        Barbarians[CurrentBarbCount].r=Position2r
        Barbarians[CurrentBarbCount].c=Position2c
        Barbarians[CurrentBarbCount].existence=1
        CurrentBarbCount=CurrentBarbCount+1
    if(keyPress=="Barb3" and CurrentBarbCount<MAX_BARBARIAN ):
        Barbarians[CurrentBarbCount].r=Position3r
        Barbarians[CurrentBarbCount].c=Position3c
        Barbarians[CurrentBarbCount].existence=1
        CurrentBarbCount=CurrentBarbCount+1
    if(keyPress == "Space" and king.health>0):
        king.attack(huts,Townhall,walls,cannons)
    if(keyPress == "Heal" and Hspell>0):
        Hspell=Hspell-1
        for barb in Barbarians:
            if(3*barb.health/2>100):
                barb.health=100
            else:
                if(barb.health>0):
                    barb.health = 3*barb.health/2
            if(3*king.health/2>300):
                king.health=300
            else:
                if(king.health>0):
                    king.health = 3*king.health/2

    if(keyPress == "Rage" and Rspell>0):
        Rspell=Rspell-1
        for barb in Barbarians:
            if(barb.health>0):
                barb.speedx=2*barb.speedx
                barb.speedy=2*barb.speedy
                barb.damage=barb.damage
            if(king.health>0):
                # king.speedx=2*king.speedx
                # king.speedy=2*king.speedy
                king.damage=king.damage*2
    
    # if(keyPress == "Replay" or game_over!=0):


    
        
    

os.system("stty echo")