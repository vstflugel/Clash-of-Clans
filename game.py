from re import L
import src.village as Base
import src.input as Input
import src.buildings as buildings
import src.walls as wall
import src.troops as troop
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

call = Input.Get()
MAX_LEVEL = 3
MAX_BARBARIAN=20
MAX_ARCHERS= 10
MAX_BALLOONS=5
Currentlevel = 0 
quit = 0
Loot1 = 0
Loot2=0
Loot3=0
LastMovement="right"
name = input("enter name of file: ")
f = open(name, 'w')
order = int(input("Which playable troop you wanna deploy('0' for King, '1' for Archer Queen: "))
while(order!=0 and order!=1):
    print("Enter Correct Input")
    order = int(input("Which playable troop you wanna deploy('0' for King, '1' for Archer Queen: "))
while quit==0:
    if(Currentlevel == 0):

        Hspell=5
        Rspell=5
        Position1r = 24
        Position1c = 15
        Position2r = 34
        Position2c = 185
        Position3r = 14
        Position3c = 185

        #Classes
        village=Base.Village()
        Townhall = buildings.TownHall()
        hut1 = buildings.Hut(5,60,13,80)
        hut2 = buildings.Hut(32,60,40,80)
        hut3 = buildings.Hut(18,140,26,160)
        hut4 = buildings.Hut(32,105,40,125)
        hut5 = buildings.Hut(5,105,13,125)
        cannon1 = buildings.Cannon(12,35,20,50)
        cannon3 = buildings.Cannon(25,35,33,50)
        king = troop.King(45,100)
        queen = troop.ArchQueen(45,100)
        w1 = buildings.WizTower(7,150,15,165)
        w2 = buildings.WizTower(30,150,38,165)

        #required variables
        kingCount = 1
        QueenCount =1
        game_over=0
        percent=0
        keyPress = ""
        CurrentBarbCount =0 
        CurrentArchCount=0
        CurrentBalloonCount=0
        CANVAS = [[Back.BLACK+" "] * village.WIDTH for _ in range(village.HEIGHT)]#
        colors =[Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.BLACK, Fore.CYAN]
        count=0
        #arrays for troops
        Barbarians=[]
        Archers =[]
        Balloons =[]

        for i in range(MAX_BARBARIAN):
            Barbarians.append(troop.Barbs(Position1r,Position1c))

        for i in range(MAX_ARCHERS):
            Archers.append(troop.Archers(Position1r,Position1c))

        for i in range(MAX_BALLOONS):
            Balloons.append(troop.Balloons(Position1r,Position1c))

        #arrays for buildings
        walls=[]
        huts=[hut1,hut2,hut3,hut4,hut5]
        cannons = [cannon1, cannon3]
        wizTowers = [w1,w2] 


        for i in range(25,176):
            walls.append(wall.Wall(3,i))    
            walls.append(wall.Wall(42,i))
        for i in range(4,42):
            walls.append(wall.Wall(i,25))
            walls.append(wall.Wall(i,175))

        def FillCanvas():
            global CANVAS
            global game_over
            global percent
            global Loot1
            village.buildCanvasFrame(CANVAS)
            village.addSpawnPoints(CANVAS)
            Townhall.AddTownhall(CANVAS)
            
            for i in range(5):
                huts[i].AddHut(CANVAS)
            
            
            
            for i in range(2):
                cannons[i].AddCannon(CANVAS)
                if(cannons[i].health>0):
                    if(order==0):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or kingCount==0):
                            cannons[i].CannonFire(Barbarians,Archers,king)
                    elif(order==1):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or QueenCount==0):
                            cannons[i].CannonFire(Barbarians,Archers,queen)

            for i in range(2):
                wizTowers[i].AddTower(CANVAS)
                if(wizTowers[i].health>0):
                    if(order==0):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or kingCount==0):
                            wizTowers[i].WizFire(Barbarians,Archers,Balloons,king)
                    elif(order==1):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or QueenCount==0):
                            wizTowers[i].WizFire(Barbarians,Archers,Balloons,queen)
                        
                    
            for wall in walls:
                wall.AddWall(CANVAS)
            c=0
            for i in range(MAX_BARBARIAN):
                if(Barbarians[i].existence==1):
                    tempClass = Barbarians[i].getTarget(huts,cannons,Townhall, wizTowers)
                    if(Barbarians[i].mov==0):
                        Barbarians[i].update(tempClass,CANVAS,walls)
                    Barbarians[i].mov =(Barbarians[i].mov+1)%2
                    Barbarians[i].display(CANVAS)
            
            for i in range(MAX_ARCHERS):
                if(Archers[i].existence==1):
                    tempClass = Archers[i].getTargetWithinRange(huts,cannons,Townhall, wizTowers)
                    if(tempClass!=-1):
                        Archers[i].Damage(tempClass)
                    else:
                        tempClass = Archers[i].getTarget(huts,cannons,Townhall, wizTowers)
                        Archers[i].update(tempClass,CANVAS,walls)
                    Archers[i].display(CANVAS)
                    


            
            for i in range(MAX_BALLOONS):
                if(Balloons[i].existence==1):
                    tempClass = Balloons[i].getTarget(huts,cannons,Townhall, wizTowers)
                    Balloons[i].update(tempClass,CANVAS,walls)
                    Balloons[i].display(CANVAS)
            # CurrentBarbCount = c
            if(kingCount==0 and order==0):
                king.display(CANVAS)
            if(QueenCount==0 and order ==1):
                queen.display(CANVAS)
            c=0
            for barb in Barbarians:
                if barb.health<=0:
                    c=c+1
            for arch in Archers:
                if(arch.health<=0):
                    c=c+1
            for balloon in Balloons:
                if(balloon.health<=0):
                    c=c+1
            if king.health<=0 and order == 0:
                c=c+1
            if queen.health<=0 and order == 1:
                c=c+1
            if c==MAX_ARCHERS+MAX_BALLOONS+MAX_BARBARIAN+1:
                game_over=1
            c=0
            percent=0
            Loot1=0
            for hut in huts:
                if hut.health<=0:
                    c=c+1
                    percent=percent+10
                    Loot1+=500
            for cannon in cannons:
                if cannon.health<=0:
                    c=c+1
                    percent=percent+7.5
            for w in wizTowers:
                if w.health<=0:
                    c=c+1
                    percent=percent+5
            if Townhall.health<=0:
                c=c+1
                Loot1+=1000
                percent=percent+25
            if c==10:
                game_over=2    

            


        def display():
            global CANVAS
            global count
            global Loot1
            global Loot2
            global Loot3

            global keyPress
            if(game_over==0):
                print("    "*village.LEFT_PADDING+colors[count]+"  ---        ---          ---")
                print("    "*village.LEFT_PADDING+colors[count]+"/          /     \      /    ")
                print("    "*village.LEFT_PADDING+colors[count]+"\       .  \     /   .  \    ")
                print("    "*village.LEFT_PADDING+colors[count]+"  ---        ---          ---")
                string = []
                for i in range(0,7):
                    string.append(' ')
                if(order == 0):
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
                elif(order==1):
                    for i in range(0,7):
                        if(queen.health/3>=50 and queen.health/3<=100 ):
                            if(i<= 0+int(queen.health/3*6/100)):
                                string[i]= Back.GREEN+' '
                            else:
                                string[i]= Back.BLACK+' '
                        if(queen.health/3>=20 and queen.health/3<50 ):
                            if(i<= 0+int(queen.health*6/300)):
                                string[i]= Back.YELLOW+' '
                            else:
                                string[i]= Back.BLACK+' '
                        if(queen.health/3>0 and queen.health/3<20 ):
                            if(i<= 0+int(queen.health/3*6/100)):
                                string[i]= Back.RED+' '
                            else:
                                string[i]= Back.BLACK+' '
                    print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"Queen's health:"+Back.BLUE+Fore.WHITE+str(" "+str(int(queen.health/3))),end=" ")
                    for i in range(7):
                        print(string[i],end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Barbarians Left:"+Back.BLUE+Fore.WHITE+str(" "+str(MAX_BARBARIAN-int(CurrentBarbCount))+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Archers Left:"+Back.BLUE+Fore.WHITE+str(" "+str(MAX_ARCHERS-int(CurrentArchCount))+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Balloons Left:"+Back.BLUE+Fore.WHITE+str(" "+str(MAX_BALLOONS-int(CurrentBalloonCount))+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Heal Spells : "+Back.BLUE+Fore.WHITE+str(" "+str(Hspell)+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Rage Spells : "+Back.BLUE+Fore.WHITE+str(" "+str(Rspell)+" "), end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Loot : "+Back.BLUE+Fore.WHITE+str(" "+str(Loot1)+"K "), end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Current Level : "+Back.BLUE+Fore.WHITE+str(" "+str(1)+" "))
                
                count=(count+1)%6
                print("\n".join(["".join(row) for row in CANVAS]), Style.RESET_ALL,end='')
                print()
            elif(game_over==1):
                print("D E F E A T")
                print("Percentage Destroyed : "+str(percent))
                print("Rewards: {}".format(Loot1+Loot2+Loot3))
                print("Press Q/q to quit the game ")

                
            elif(game_over==2):
                print("V I C T O R Y")
                print("Percentage Destroyed : "+str(percent))
                print("Current Rewards: {}".format(Loot1+Loot2+Loot3))
                print("Press N/n to go to next level")
                print("Press Q/q to quit the game ")





        t=1

        # replay feature
        

        # os.system("stty -echo")

        while(keyPress != "q"):
            os.system("clear")
            if(game_over==0):
                FillCanvas()
            display()
            # if(game_over==0):
            keyPress= call.get_input(timeout=0.1)
            if(not(keyPress is None)):
                f.write(keyPress)
                f.write('@')
            if(order==0 and king.health>0):
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
                    LastMovement = keyPress
                if(keyPress == "attack"):
                    king.attack(huts, Townhall, walls, cannons, wizTowers)
            elif(order==1 and queen.health>0):
                if(keyPress=="King1" and QueenCount==1):
                    queen.r=Position1r
                    queen.c=Position1c
                    QueenCount=0
                if(keyPress=="King2" and QueenCount==1):
                    queen.r=Position2r
                    queen.c=Position2c
                    QueenCount=0
                if(keyPress=="King3" and QueenCount==1):
                    queen.r=Position3r
                    queen.c=Position3c
                    QueenCount=0    
                if(keyPress == "left" or keyPress == "right" or keyPress == "up" or keyPress=="down" and QueenCount==0):
                    queen.update(keyPress,CANVAS)
                    LastMovement = keyPress
                if(keyPress == "attack"):
                    queen.attack(huts, Townhall, walls, cannons, wizTowers,LastMovement)
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
            if(keyPress=="Arch1" and CurrentArchCount<MAX_ARCHERS):
                Archers[CurrentArchCount].r=Position1r
                Archers[CurrentArchCount].c=Position1c
                Archers[CurrentArchCount].existence=1
                CurrentArchCount=CurrentArchCount+1
            if(keyPress=="Arch2" and CurrentArchCount<MAX_ARCHERS ):
                Archers[CurrentArchCount].r=Position2r
                Archers[CurrentArchCount].c=Position2c
                Archers[CurrentArchCount].existence=1
                CurrentArchCount=CurrentArchCount+1
            if(keyPress=="Arch3" and CurrentArchCount<MAX_ARCHERS ):
                Archers[CurrentArchCount].r=Position3r
                Archers[CurrentArchCount].c=Position3c
                Archers[CurrentArchCount].existence=1
                CurrentArchCount=CurrentArchCount+1
            if(keyPress=="Ball1" and CurrentBalloonCount<MAX_BALLOONS):
                Balloons[CurrentBalloonCount].r=Position1r
                Balloons[CurrentBalloonCount].c=Position1c
                Balloons[CurrentBalloonCount].existence=1
                CurrentBalloonCount=CurrentBalloonCount+1
            if(keyPress=="Ball2" and CurrentBalloonCount<MAX_BALLOONS ):
                Balloons[CurrentBalloonCount].r=Position2r
                Balloons[CurrentBalloonCount].c=Position2c
                Balloons[CurrentBalloonCount].existence=1
                CurrentBalloonCount=CurrentBalloonCount+1
            if(keyPress=="Ball3" and CurrentBalloonCount<MAX_BALLOONS ):
                Balloons[CurrentBalloonCount].r=Position3r
                Balloons[CurrentBalloonCount].c=Position3c
                Balloons[CurrentBalloonCount].existence=1
                CurrentBalloonCount=CurrentBalloonCount+1
            if(keyPress == "Heal" and Hspell>0):
                Hspell=Hspell-1
                for barb in Barbarians:
                    if(barb.health>66):
                        barb.health=100
                    else:
                        if(barb.health>0):
                            barb.health = 3*barb.health/2
                    if(king.health>200):
                        king.health=300
                    else:
                        if(king.health>0):
                            king.health = 3*king.health/2
                    if(queen.health>200):
                        queen.health=300
                    else:
                        if(queen.health>0):
                            queen.health = 3*queen.health/2
        #______________________TO BE DONE_______________________
            if (keyPress == "Next" and game_over!=0):
                Currentlevel= (Currentlevel+1)%3
                break
            if keyPress == "q":
                quit=1
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
            
            
        # __________________________________________________________

        # os.system("stty echo")

    elif(Currentlevel == 1):

        Hspell=5
        Rspell=5
        Position1r = 24
        Position1c = 15
        Position2r = 34
        Position2c = 185
        Position3r = 14
        Position3c = 185

        #Classes
        village=Base.Village()
        Townhall = buildings.TownHall()
        hut1 = buildings.Hut(5,60,13,80)
        hut2 = buildings.Hut(32,60,40,80)
        hut3 = buildings.Hut(18,140,26,160)
        hut4 = buildings.Hut(32,110,40,130)
        hut5 = buildings.Hut(5,110,13,130)
        cannon1 = buildings.Cannon(12,35,20,50)
        cannon2 = buildings.Cannon(5,87,13,102)
        cannon3 = buildings.Cannon(25,35,33,50)

        king = troop.King(45,100)
        queen = troop.ArchQueen(45,100)
        w1 = buildings.WizTower(7,150,15,165)
        w2 = buildings.WizTower(30,150,38,165)
        w3 = buildings.WizTower(32,87,40,102)


        #required variables
        kingCount = 1
        QueenCount =1
        game_over=0#
        percent=0
        keyPress = ""#
        CurrentBarbCount =0 
        CurrentArchCount=0
        CurrentBalloonCount=0
        CANVAS = [[Back.BLACK+" "] * village.WIDTH for _ in range(village.HEIGHT)]#
        colors =[Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.BLACK, Fore.CYAN]
        count=0#
        #arrays for troops
        Barbarians=[]
        Archers =[]
        Balloons =[]

        for i in range(MAX_BARBARIAN):
            Barbarians.append(troop.Barbs(Position1r,Position1c))

        for i in range(MAX_ARCHERS):
            Archers.append(troop.Archers(Position1r,Position1c))

        for i in range(MAX_BALLOONS):
            Balloons.append(troop.Balloons(Position1r,Position1c))

        #arrays for buildings
        walls=[]
        huts=[hut1,hut2,hut3,hut4,hut5]
        cannons = [cannon1,cannon2, cannon3]
        wizTowers = [w1,w2,w3] 


        for i in range(25,176):
            walls.append(wall.Wall(3,i))    
            walls.append(wall.Wall(42,i))
        for i in range(4,42):
            walls.append(wall.Wall(i,25))
            walls.append(wall.Wall(i,175))

        def FillCanvas():
            global CANVAS
            global game_over
            global percent
            global Loot2
            village.buildCanvasFrame(CANVAS)
            village.addSpawnPoints(CANVAS)
            Townhall.AddTownhall(CANVAS)
            
            for i in range(5):
                huts[i].AddHut(CANVAS)
            
            
            
            for i in range(3):
                cannons[i].AddCannon(CANVAS)
                if(cannons[i].health>0):
                    if(order==0):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or kingCount==0):
                            cannons[i].CannonFire(Barbarians,Archers,king)
                    elif(order==1):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or QueenCount==0):
                            cannons[i].CannonFire(Barbarians,Archers,queen)

            for i in range(3):
                wizTowers[i].AddTower(CANVAS)
                if(wizTowers[i].health>0):
                    if(order==0):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or kingCount==0):
                            wizTowers[i].WizFire(Barbarians,Archers,Balloons,king)
                    elif(order==1):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or QueenCount==0):
                            wizTowers[i].WizFire(Barbarians,Archers,Balloons,queen)
                        
                    
            for wall in walls:
                wall.AddWall(CANVAS)
            c=0
            for i in range(MAX_BARBARIAN):
                if(Barbarians[i].existence==1):
                    tempClass = Barbarians[i].getTarget(huts,cannons,Townhall, wizTowers)
                    if(Barbarians[i].mov==0):
                        Barbarians[i].update(tempClass,CANVAS,walls)
                    Barbarians[i].mov =(Barbarians[i].mov+1)%2
                    Barbarians[i].display(CANVAS)
            
            for i in range(MAX_ARCHERS):
                if(Archers[i].existence==1):
                    tempClass = Archers[i].getTargetWithinRange(huts,cannons,Townhall, wizTowers)
                    if(tempClass!=-1):
                        Archers[i].Damage(tempClass)
                    else:
                        tempClass = Archers[i].getTarget(huts,cannons,Townhall, wizTowers)
                        Archers[i].update(tempClass,CANVAS,walls)
                    Archers[i].display(CANVAS)
                    


            
            for i in range(MAX_BALLOONS):
                if(Balloons[i].existence==1):
                    tempClass = Balloons[i].getTarget(huts,cannons,Townhall, wizTowers)
                    Balloons[i].update(tempClass,CANVAS,walls)
                    Balloons[i].display(CANVAS)
            # CurrentBarbCount = c
            if(kingCount==0 and order==0):
                king.display(CANVAS)
            if(QueenCount==0 and order ==1):
                queen.display(CANVAS)
            c=0
            for barb in Barbarians:
                if barb.health<=0:
                    c=c+1
            for arch in Archers:
                if(arch.health<=0):
                    c=c+1
            for balloon in Balloons:
                if(balloon.health<=0):
                    c=c+1
            if king.health<=0 and order == 0:
                c=c+1
            if queen.health<=0 and order == 1:
                c=c+1
            if c==MAX_ARCHERS+MAX_BALLOONS+MAX_BARBARIAN+1:
                game_over=1
            c=0
            percent=0
            Loot2=0
            for hut in huts:
                if hut.health<=0:
                    c=c+1
                    percent=percent+10
                    Loot2+=500
            for cannon in cannons:
                if cannon.health<=0:
                    c=c+1
                    percent=percent+5
            for w in wizTowers:
                if w.health<=0:
                    c=c+1
                    percent=percent+5
            if Townhall.health<=0:
                c=c+1
                Loot2+=1000
                percent=percent+20
            if c==12:
                game_over=2    

            


        def display():
            global CANVAS
            global count
            global keyPress
            global Loot1
            global Loot2
            global Loot3
            if(game_over==0):
                print("    "*village.LEFT_PADDING+colors[count]+"  ---        ---          ---")
                print("    "*village.LEFT_PADDING+colors[count]+"/          /     \      /    ")
                print("    "*village.LEFT_PADDING+colors[count]+"\       .  \     /   .  \    ")
                print("    "*village.LEFT_PADDING+colors[count]+"  ---        ---          ---")
                string = []
                for i in range(0,7):
                    string.append(' ')
                if(order == 0):
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
                elif(order==1):
                    for i in range(0,7):
                        if(queen.health/3>=50 and queen.health/3<=100 ):
                            if(i<= 0+int(queen.health/3*6/100)):
                                string[i]= Back.GREEN+' '
                            else:
                                string[i]= Back.BLACK+' '
                        if(queen.health/3>=20 and queen.health/3<50 ):
                            if(i<= 0+int(queen.health*6/300)):
                                string[i]= Back.YELLOW+' '
                            else:
                                string[i]= Back.BLACK+' '
                        if(queen.health/3>0 and queen.health/3<20 ):
                            if(i<= 0+int(queen.health/3*6/100)):
                                string[i]= Back.RED+' '
                            else:
                                string[i]= Back.BLACK+' '
                    print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"Queen's health:"+Back.BLUE+Fore.WHITE+str(" "+str(int(queen.health/3))),end=" ")
                    for i in range(7):
                        print(string[i],end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Barbarians Left:"+Back.BLUE+Fore.WHITE+str(" "+str(MAX_BARBARIAN-int(CurrentBarbCount))+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Archers Left:"+Back.BLUE+Fore.WHITE+str(" "+str(MAX_ARCHERS-int(CurrentArchCount))+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Balloons Left:"+Back.BLUE+Fore.WHITE+str(" "+str(MAX_BALLOONS-int(CurrentBalloonCount))+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Heal Spells : "+Back.BLUE+Fore.WHITE+str(" "+str(Hspell)+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Rage Spells : "+Back.BLUE+Fore.WHITE+str(" "+str(Rspell)+" "), end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Loot : "+Back.BLUE+Fore.WHITE+str(" "+str(Loot2)+"K "), end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Current Level : "+Back.BLUE+Fore.WHITE+str(" "+str(2)+" "))
                
                count=(count+1)%6
                print("\n".join(["".join(row) for row in CANVAS]), Style.RESET_ALL,end='')
                print()
            elif(game_over==1):
                print("D E F E A T")
                print("Percentage Destroyed : "+str(percent))
                print("Rewards: {}".format(Loot1+Loot2+Loot3))
                print("Press Q/q to quit the game ")


                
            elif(game_over==2):
                print("V I C T O R Y")
                print("Percentage Destroyed : "+str(percent))
                print("Current Rewards: {}".format(Loot1+Loot2+Loot3))
                print("Press N/n to go to next level")
                print("Press Q/q to quit the game ")






        t=1

        # replay feature
        

        # os.system("stty -echo")

        while(keyPress != "q"):
            os.system("clear")
            if(game_over==0):
                FillCanvas()
            display()
            # if(game_over==0):
            keyPress= call.get_input(timeout=0.1)
            if(not(keyPress is None)):
                f.write(keyPress)
                f.write('@')
            if(order==0 and king.health>0):
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
                    LastMovement=keyPress
                if(keyPress == "attack"):
                    king.attack(huts, Townhall, walls, cannons, wizTowers)
            elif(order==1 and queen.health>0):
                if(keyPress=="King1" and QueenCount==1):
                    queen.r=Position1r
                    queen.c=Position1c
                    QueenCount=0
                if(keyPress=="King2" and QueenCount==1):
                    queen.r=Position2r
                    queen.c=Position2c
                    QueenCount=0
                if(keyPress=="King3" and QueenCount==1):
                    queen.r=Position3r
                    queen.c=Position3c
                    QueenCount=0    
                if(keyPress == "left" or keyPress == "right" or keyPress == "up" or keyPress=="down" and QueenCount==0):
                    queen.update(keyPress,CANVAS)
                    LastMovement=keyPress
                if(keyPress == "attack"):
                    queen.attack(huts, Townhall, walls, cannons, wizTowers,LastMovement)
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
            if(keyPress=="Arch1" and CurrentArchCount<MAX_ARCHERS):
                Archers[CurrentArchCount].r=Position1r
                Archers[CurrentArchCount].c=Position1c
                Archers[CurrentArchCount].existence=1
                CurrentArchCount=CurrentArchCount+1
            if(keyPress=="Arch2" and CurrentArchCount<MAX_ARCHERS ):
                Archers[CurrentArchCount].r=Position2r
                Archers[CurrentArchCount].c=Position2c
                Archers[CurrentArchCount].existence=1
                CurrentArchCount=CurrentArchCount+1
            if(keyPress=="Arch3" and CurrentArchCount<MAX_ARCHERS ):
                Archers[CurrentArchCount].r=Position3r
                Archers[CurrentArchCount].c=Position3c
                Archers[CurrentArchCount].existence=1
                CurrentArchCount=CurrentArchCount+1
            if(keyPress=="Ball1" and CurrentBalloonCount<MAX_BALLOONS):
                Balloons[CurrentBalloonCount].r=Position1r
                Balloons[CurrentBalloonCount].c=Position1c
                Balloons[CurrentBalloonCount].existence=1
                CurrentBalloonCount=CurrentBalloonCount+1
            if(keyPress=="Ball2" and CurrentBalloonCount<MAX_BALLOONS ):
                Balloons[CurrentBalloonCount].r=Position2r
                Balloons[CurrentBalloonCount].c=Position2c
                Balloons[CurrentBalloonCount].existence=1
                CurrentBalloonCount=CurrentBalloonCount+1
            if(keyPress=="Ball3" and CurrentBalloonCount<MAX_BALLOONS ):
                Balloons[CurrentBalloonCount].r=Position3r
                Balloons[CurrentBalloonCount].c=Position3c
                Balloons[CurrentBalloonCount].existence=1
                CurrentBalloonCount=CurrentBalloonCount+1
            if(keyPress == "Heal" and Hspell>0):
                Hspell=Hspell-1
                for barb in Barbarians:
                    if(barb.health>66):
                        barb.health=100
                    else:
                        if(barb.health>0):
                            barb.health = 3*barb.health/2
                    if(king.health>200):
                        king.health=300
                    else:
                        if(king.health>0):
                            king.health = 3*king.health/2
                    if(queen.health>200):
                        queen.health=300
                    else:
                        if(queen.health>0):
                            queen.health = 3*queen.health/2
            if (keyPress == "Next" and game_over!=0):
                Currentlevel= (Currentlevel+1)%3
                break
            if keyPress == "q":
                quit=1
        #______________________TO BE DONE_______________________
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
            
        # __________________________________________________________
        # os.system(stty echo)

    elif(Currentlevel == 2):

        Hspell=5
        Rspell=5
        Position1r = 24
        Position1c = 15
        Position2r = 34
        Position2c = 185
        Position3r = 14
        Position3c = 185

        #Classes
        village=Base.Village()
        Townhall = buildings.TownHall()
        hut1 = buildings.Hut(5,60,13,80)
        hut2 = buildings.Hut(32,60,40,80)
        hut3 = buildings.Hut(18,140,26,160)
        hut4 = buildings.Hut(32,110,40,130)
        hut5 = buildings.Hut(5,110,13,130)
        cannon1 = buildings.Cannon(12,35,20,50)
        cannon2 = buildings.Cannon(5,87,13,102)
        cannon3 = buildings.Cannon(25,35,33,50)
        cannon4 = buildings.Cannon(18,120,26,135)
        king = troop.King(45,100)
        queen = troop.ArchQueen(45,100)
        w1 = buildings.WizTower(7,150,15,165)
        w2 = buildings.WizTower(30,150,38,165)
        w3 = buildings.WizTower(32,87,40,102)
        w4 = buildings.WizTower(18,55,26,70)
        #required variables
        kingCount = 1
        QueenCount =1
        game_over=0
        percent=0
        keyPress = ""
        CurrentBarbCount =0 
        CurrentArchCount=0
        CurrentBalloonCount=0
        CANVAS = [[Back.BLACK+" "] * village.WIDTH for _ in range(village.HEIGHT)]
        colors =[Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.BLACK, Fore.CYAN]
        count=0
        #arrays for troops
        Barbarians=[]
        Archers =[]
        Balloons =[]

        for i in range(MAX_BARBARIAN):
            Barbarians.append(troop.Barbs(Position1r,Position1c))

        for i in range(MAX_ARCHERS):
            Archers.append(troop.Archers(Position1r,Position1c))

        for i in range(MAX_BALLOONS):
            Balloons.append(troop.Balloons(Position1r,Position1c))

        #arrays for buildings
        walls=[]
        huts=[hut1,hut2,hut3,hut4,hut5]
        cannons = [cannon1,cannon2, cannon3,cannon4]
        wizTowers = [w1,w2,w3,w4] 


        for i in range(25,176):
            walls.append(wall.Wall(3,i))    
            walls.append(wall.Wall(42,i))
        for i in range(4,42):
            walls.append(wall.Wall(i,25))
            walls.append(wall.Wall(i,175))

        def FillCanvas():
            global CANVAS
            global game_over
            global Loot3
            global percent
            village.buildCanvasFrame(CANVAS)
            village.addSpawnPoints(CANVAS)
            Townhall.AddTownhall(CANVAS)
            
            for i in range(5):
                huts[i].AddHut(CANVAS)
            
            
            
            for i in range(4):
                cannons[i].AddCannon(CANVAS)
                if(cannons[i].health>0):
                    if(order==0):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or kingCount==0):
                            cannons[i].CannonFire(Barbarians,Archers,king)
                    elif(order==1):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or QueenCount==0):
                            cannons[i].CannonFire(Barbarians,Archers,queen)

            for i in range(4):
                wizTowers[i].AddTower(CANVAS)
                if(wizTowers[i].health>0):
                    if(order==0):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or kingCount==0):
                            wizTowers[i].WizFire(Barbarians,Archers,Balloons,king)
                    elif(order==1):
                        if(CurrentBarbCount>0 or CurrentArchCount>0 or CurrentBalloonCount>0 or QueenCount==0):
                            wizTowers[i].WizFire(Barbarians,Archers,Balloons,queen)
                        
                    
            for wall in walls:
                wall.AddWall(CANVAS)
            c=0
            for i in range(MAX_BARBARIAN):
                if(Barbarians[i].existence==1):
                    tempClass = Barbarians[i].getTarget(huts,cannons,Townhall, wizTowers)
                    if(Barbarians[i].mov==0):
                        Barbarians[i].update(tempClass,CANVAS,walls)
                    Barbarians[i].mov =(Barbarians[i].mov+1)%2
                    Barbarians[i].display(CANVAS)
            
            for i in range(MAX_ARCHERS):
                if(Archers[i].existence==1):
                    tempClass = Archers[i].getTargetWithinRange(huts,cannons,Townhall, wizTowers)
                    if(tempClass!=-1):
                        Archers[i].Damage(tempClass)
                    else:
                        tempClass = Archers[i].getTarget(huts,cannons,Townhall, wizTowers)
                        Archers[i].update(tempClass,CANVAS,walls)
                    Archers[i].display(CANVAS)
                    


            
            for i in range(MAX_BALLOONS):
                if(Balloons[i].existence==1):
                    tempClass = Balloons[i].getTarget(huts,cannons,Townhall, wizTowers)
                    Balloons[i].update(tempClass,CANVAS,walls)
                    Balloons[i].display(CANVAS)
            # CurrentBarbCount = c
            if(kingCount==0 and order==0):
                king.display(CANVAS)
            if(QueenCount==0 and order ==1):
                queen.display(CANVAS)
            c=0
            for barb in Barbarians:
                if barb.health<=0:
                    c=c+1
            for arch in Archers:
                if(arch.health<=0):
                    c=c+1
            for balloon in Balloons:
                if(balloon.health<=0):
                    c=c+1
            if king.health<=0 and order == 0:
                c=c+1
            if queen.health<=0 and order == 1:
                c=c+1
            if c==MAX_ARCHERS+MAX_BALLOONS+MAX_BARBARIAN+1:
                game_over=1
            c=0
            percent=0
            Loot3=0
            for hut in huts:
                if hut.health<=0:
                    c=c+1
                    percent=percent+10
                    Loot3+=500
            for cannon in cannons:
                if cannon.health<=0:
                    c=c+1
                    percent=percent+3.75
            for w in wizTowers:
                if w.health<=0:
                    c=c+1
                    percent=percent+2.5
            if Townhall.health<=0:
                c=c+1
                Loot3+=1000
                percent=percent+25
            if c==14:
                game_over=2    

            


        def display():
            global CANVAS
            global count
            global keyPress
            global Loot3
            global Loot2
            global Loot1
            if(game_over==0):
                print("    "*village.LEFT_PADDING+colors[count]+"  ---        ---          ---")
                print("    "*village.LEFT_PADDING+colors[count]+"/          /     \      /    ")
                print("    "*village.LEFT_PADDING+colors[count]+"\       .  \     /   .  \    ")
                print("    "*village.LEFT_PADDING+colors[count]+"  ---        ---          ---")
                string = []
                for i in range(0,7):
                    string.append(' ')
                if(order == 0):
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
                elif(order==1):
                    for i in range(0,7):
                        if(queen.health/3>=50 and queen.health/3<=100 ):
                            if(i<= 0+int(queen.health/3*6/100)):
                                string[i]= Back.GREEN+' '
                            else:
                                string[i]= Back.BLACK+' '
                        if(queen.health/3>=20 and queen.health/3<50 ):
                            if(i<= 0+int(queen.health*6/300)):
                                string[i]= Back.YELLOW+' '
                            else:
                                string[i]= Back.BLACK+' '
                        if(queen.health/3>0 and queen.health/3<20 ):
                            if(i<= 0+int(queen.health/3*6/100)):
                                string[i]= Back.RED+' '
                            else:
                                string[i]= Back.BLACK+' '
                    print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"Queen's health:"+Back.BLUE+Fore.WHITE+str(" "+str(int(queen.health/3))),end=" ")
                    for i in range(7):
                        print(string[i],end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Barbarians Left:"+Back.BLUE+Fore.WHITE+str(" "+str(MAX_BARBARIAN-int(CurrentBarbCount))+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Archers Left:"+Back.BLUE+Fore.WHITE+str(" "+str(MAX_ARCHERS-int(CurrentArchCount))+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+" Balloons Left:"+Back.BLUE+Fore.WHITE+str(" "+str(MAX_BALLOONS-int(CurrentBalloonCount))+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Heal Spells : "+Back.BLUE+Fore.WHITE+str(" "+str(Hspell)+" "),end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Rage Spells : "+Back.BLUE+Fore.WHITE+str(" "+str(Rspell)+" "), end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Loot : "+Back.BLUE+Fore.WHITE+str(" "+str(Loot3)+"K "), end="")
                print(Back.LIGHTBLACK_EX+Fore.LIGHTCYAN_EX+"  Current Level : "+Back.BLUE+Fore.WHITE+str(" "+str(3)+" "))
                
                count=(count+1)%6
                print("\n".join(["".join(row) for row in CANVAS]), Style.RESET_ALL,end='')
                print()
            elif(game_over==1):
                print("D E F E A T")
                print("Percentage Destroyed : "+str(percent))
                print("Rewards: {}".format(Loot1+Loot2+Loot3))
                print("Press Q/q to quit the game ")


                
            elif(game_over==2):
                print("V I C T O R Y")
                print("Percentage Destroyed : "+str(percent))
                print("Congratulations you successfully Completed all the levels")
                print("Final Rewards: {}".format(Loot1+Loot2+Loot3))
                Loot1=0
                Loot2=0
                Loot3=0
                print("Press N/n to restart the game ")
                print("Press Q/q to quit the game ")





        t=1

        # replay feature
        

        # os.system("stty -echo")

        while(keyPress != "q"):
            os.system("clear")
            if(game_over==0):
                FillCanvas()
            display()
            # if(game_over==0):
            keyPress= call.get_input(timeout=0.1)
            if(not(keyPress is None)):
                f.write(keyPress)
                f.write('@')
            if(order==0 and king.health>0):
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
                    king.attack(huts, Townhall, walls, cannons, wizTowers)
            elif(order==1 and queen.health>0):
                if(keyPress=="King1" and QueenCount==1):
                    queen.r=Position1r
                    queen.c=Position1c
                    QueenCount=0
                if(keyPress=="King2" and QueenCount==1):
                    queen.r=Position2r
                    queen.c=Position2c
                    QueenCount=0
                if(keyPress=="King3" and QueenCount==1):
                    queen.r=Position3r
                    queen.c=Position3c
                    QueenCount=0    
                if(keyPress == "left" or keyPress == "right" or keyPress == "up" or keyPress=="down" and QueenCount==0):
                    queen.update(keyPress,CANVAS)
                    LastMovement=keyPress
                if(keyPress == "attack"):
                    queen.attack(huts, Townhall, walls, cannons, wizTowers,LastMovement)
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
            if(keyPress=="Arch1" and CurrentArchCount<MAX_ARCHERS):
                Archers[CurrentArchCount].r=Position1r
                Archers[CurrentArchCount].c=Position1c
                Archers[CurrentArchCount].existence=1
                CurrentArchCount=CurrentArchCount+1
            if(keyPress=="Arch2" and CurrentArchCount<MAX_ARCHERS ):
                Archers[CurrentArchCount].r=Position2r
                Archers[CurrentArchCount].c=Position2c
                Archers[CurrentArchCount].existence=1
                CurrentArchCount=CurrentArchCount+1
            if(keyPress=="Arch3" and CurrentArchCount<MAX_ARCHERS ):
                Archers[CurrentArchCount].r=Position3r
                Archers[CurrentArchCount].c=Position3c
                Archers[CurrentArchCount].existence=1
                CurrentArchCount=CurrentArchCount+1
            if(keyPress=="Ball1" and CurrentBalloonCount<MAX_BALLOONS):
                Balloons[CurrentBalloonCount].r=Position1r
                Balloons[CurrentBalloonCount].c=Position1c
                Balloons[CurrentBalloonCount].existence=1
                CurrentBalloonCount=CurrentBalloonCount+1
            if(keyPress=="Ball2" and CurrentBalloonCount<MAX_BALLOONS ):
                Balloons[CurrentBalloonCount].r=Position2r
                Balloons[CurrentBalloonCount].c=Position2c
                Balloons[CurrentBalloonCount].existence=1
                CurrentBalloonCount=CurrentBalloonCount+1
            if(keyPress=="Ball3" and CurrentBalloonCount<MAX_BALLOONS ):
                Balloons[CurrentBalloonCount].r=Position3r
                Balloons[CurrentBalloonCount].c=Position3c
                Balloons[CurrentBalloonCount].existence=1
                CurrentBalloonCount=CurrentBalloonCount+1
            if(keyPress == "Heal" and Hspell>0):
                Hspell=Hspell-1
                for barb in Barbarians:
                    if(barb.health>66):
                        barb.health=100
                    else:
                        if(barb.health>0):
                            barb.health = 3*barb.health/2
                    if(king.health>200):
                        king.health=300
                    else:
                        if(king.health>0):
                            king.health = 3*king.health/2
                    if(queen.health>200):
                        queen.health=300
                    else:
                        if(queen.health>0):
                            queen.health = 3*queen.health/2
            if (keyPress == "Next" and game_over!=0):
                Currentlevel= (Currentlevel+1)%3
                break
            if keyPress == "q":
                quit=1
        #______________________TO BE DONE_______________________
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
            

        # __________________________________________________________
        # os.system(stty echo)

