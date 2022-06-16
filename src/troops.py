import colorama
from colorama import Fore, Back, Style
import numpy as np
from sympy import re
from src.walls import Wall

colorama.init(autoreset=True)

def dis(x1,y1,x2,y2):
    return(np.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))

def doOverlap(l1x, l1y, r1x, r1y, l2x,l2y, r2x,r2y):
    if(l1y >= r2y or l2y >= r1y):
        return False 
    if(l2x >= r1x or l1x >= r2x):
        return False
 
    return True

class Troop:
    def __init__(self, x, y):
        self.r=x
        self.c=y
        self.speedx = 1
        self.speedy = 1
        

class King(Troop):
    def __init__(self,x,y):
        Troop.__init__(self,x, y)
        self.health = 300
        self.damage = 50
        self.length = 4
        self.height = 5
    
    def display(self, canvas):
        if(self.health>0):
            canvas[self.r+2][self.c]=Fore.RED+Style.BRIGHT+' '
            canvas[self.r+2][self.c+1]=Fore.RED+Style.BRIGHT+'⛑'
            canvas[self.r+2][self.c+2]=Fore.RED+Style.BRIGHT+' '
            canvas[self.r+2][self.c+3]=Fore.RED+Style.BRIGHT+' '
            canvas[self.r+3][self.c-1]=Fore.RED+Style.BRIGHT+'⛏'
            canvas[self.r+3][self.c+1]=Fore.RED+Style.BRIGHT+'/'
            canvas[self.r+3][self.c+2]=Fore.RED+Style.BRIGHT+'|'
            canvas[self.r+3][self.c+3]=Fore.RED+Style.BRIGHT+'\\'
            canvas[self.r+4][self.c]=Fore.RED+Style.BRIGHT+' '
            canvas[self.r+4][self.c+1]=Fore.RED+Style.BRIGHT+' '
            canvas[self.r+4][self.c+2]=Fore.RED+Style.BRIGHT+'⚻'
            canvas[self.r+4][self.c+3]=Fore.RED+Style.BRIGHT+' '
        else:
            self.speedx=0
            self.speedy=0
            # canvas[self.r+2][self.c]=Back.BLACK+' '
            # canvas[self.r+2][self.c+1]=Back.BLACK+' '
            # canvas[self.r+2][self.c+2]=Back.BLACK+' '
            # canvas[self.r+2][self.c+3]=Back.BLACK+' '
            # canvas[self.r+3][self.c-1]=Back.BLACK+' '
            # canvas[self.r+3][self.c+1]=Back.BLACK+' '
            # canvas[self.r+3][self.c+2]=Back.BLACK+' '
            # canvas[self.r+3][self.c+3]=Back.BLACK+' '
            # canvas[self.r+4][self.c]=Back.BLACK+' '
            # canvas[self.r+4][self.c+1]=Back.BLACK+' '
            # canvas[self.r+4][self.c+2]=Back.BLACK+' '
            # canvas[self.r+4][self.c+3]=Back.BLACK+' '

    def update(self,string,canvas):
        canvas[self.r+2][self.c]=Back.BLACK+' '
        canvas[self.r+2][self.c+1]=Back.BLACK+' '
        canvas[self.r+2][self.c+2]=Back.BLACK+' '
        canvas[self.r+2][self.c+3]=Back.BLACK+' '
        canvas[self.r+3][self.c-1]=Back.BLACK+' '
        canvas[self.r+3][self.c+1]=Back.BLACK+' '
        canvas[self.r+3][self.c+2]=Back.BLACK+' '
        canvas[self.r+3][self.c+3]=Back.BLACK+' '
        canvas[self.r+4][self.c]=Back.BLACK+' '
        canvas[self.r+4][self.c+1]=Back.BLACK+' '
        canvas[self.r+4][self.c+2]=Back.BLACK+' '
        canvas[self.r+4][self.c+3]=Back.BLACK+' '
        if(string=="left" and canvas[self.r+2][self.c-self.speedx-1]==str(Back.BLACK+' ') and canvas[self.r+4][self.c-self.speedx-1]==str(Back.BLACK+' ')):
            self.c= self.c-self.speedx
        elif(string=="right" and canvas[self.r+3][self.c+self.speedx+3]==str(Back.BLACK+' ') and canvas[self.r+2][self.c+self.speedx+3]==str(Back.BLACK+' ') and canvas[self.r+4][self.c+self.speedx+3]==str(Back.BLACK+' ')):
            self.c= self.c+self.speedx
        elif(string=="up" and canvas[self.r-self.speedy+2][self.c-1]==str(Back.BLACK + ' ') and canvas[self.r-self.speedy+2][self.c+3]==str(Back.BLACK + ' ')):
            self.r = self.r-self.speedy
        elif(string=="down" and canvas[self.r+self.speedy+4][self.c-1]==str(Back.BLACK + ' ') and canvas[self.r+self.speedy+4][self.c+3]==str(Back.BLACK + ' ')):
            self.r = self.r+self.speedy

    def attack(self, huts, Townhall, walls,cannons, wizTowers):
        # checking for walls
        for wall in walls:
            if(wall.row<= self.r+6 and wall.row>=self.r and wall.column>=self.c-3 and wall.column<=self.c+5 and wall.health>0):
                wall.health=wall.health -50
        for hut in huts:
            if(doOverlap(self.r,self.c-3,self.r+6,self.c+5,hut.UpperLeftRow,hut.UpperLeftColumn,hut.LowerRightRow,hut.LowerRightColumn )and hut.health>0):
                hut.health=hut.health -50
        for cannon in cannons:
            if(doOverlap(self.r,self.c-3,self.r+6,self.c+5,cannon.UpperLeftRow,cannon.UpperLeftColumn,cannon.LowerRightRow,cannon.LowerRightColumn) and cannon.health>0):
                cannon.health=cannon.health -50
        for wiz in wizTowers:
            if(doOverlap(self.r,self.c-3,self.r+6,self.c+5,wiz.UpperLeftRow,wiz.UpperLeftColumn,wiz.LowerRightRow,wiz.LowerRightColumn) and wiz.health>0):
                wiz.health=wiz.health -50
        if(doOverlap(self.r,self.c-3,self.r+6,self.c+5,Townhall.UpperLeftRow,Townhall.UpperLeftColumn,Townhall.LowerRightRow,Townhall.LowerRightColumn)and Townhall.health>0):
            Townhall.health = Townhall.health - 50
        
class ArchQueen(Troop):
    def __init__(self,x,y):
        Troop.__init__(self,x, y)
        self.health = 300
        self.damage = 30
        self.length = 4
        self.height = 5
    def display(self, canvas):
        if(self.health>0):
            canvas[self.r+2][self.c]=Fore.BLUE+Style.BRIGHT+' '
            canvas[self.r+2][self.c+1]=Fore.BLUE+Style.BRIGHT+'👸'
            canvas[self.r+2][self.c+2]=Fore.BLUE+Style.BRIGHT+' '
            canvas[self.r+2][self.c+3]=Fore.BLUE+Style.BRIGHT+''
            canvas[self.r+3][self.c-1]=Fore.GREEN+Style.BRIGHT+'⇱'
            canvas[self.r+3][self.c+1]=Fore.BLUE+Style.BRIGHT+'/'
            canvas[self.r+3][self.c+2]=Fore.BLUE+Style.BRIGHT+'|'
            canvas[self.r+3][self.c+3]=Fore.BLUE+Style.BRIGHT+'\\'
            canvas[self.r+4][self.c]=Fore.BLUE+Style.BRIGHT+' '
            canvas[self.r+4][self.c+1]=Fore.BLUE+Style.BRIGHT+' '
            canvas[self.r+4][self.c+2]=Fore.BLUE+Style.BRIGHT+'⚻'
            canvas[self.r+4][self.c+3]=Fore.BLUE+Style.BRIGHT+' '
        else:
            self.speedx=0
            self.speedy=0
            # canvas[self.r+2][self.c]=Back.BLACK+' '
            # canvas[self.r+2][self.c+1]=Back.BLACK+' '
            # canvas[self.r+2][self.c+2]=Back.BLACK+' '
            # canvas[self.r+2][self.c+3]=Back.BLACK+' '
            # canvas[self.r+3][self.c-1]=Back.BLACK+' '
            # canvas[self.r+3][self.c+1]=Back.BLACK+' '
            # canvas[self.r+3][self.c+2]=Back.BLACK+' '
            # canvas[self.r+3][self.c+3]=Back.BLACK+' '
            # canvas[self.r+4][self.c]=Back.BLACK+' '
            # canvas[self.r+4][self.c+1]=Back.BLACK+' '
            # canvas[self.r+4][self.c+2]=Back.BLACK+' '
            # canvas[self.r+4][self.c+3]=Back.BLACK+' '

    def update(self,string,canvas):
        canvas[self.r+2][self.c]=Back.BLACK+' '
        canvas[self.r+2][self.c+1]=Back.BLACK+' '
        canvas[self.r+2][self.c+2]=Back.BLACK+' '
        canvas[self.r+2][self.c+3]=Back.BLACK+' '
        canvas[self.r+3][self.c-1]=Back.BLACK+' '
        canvas[self.r+3][self.c+1]=Back.BLACK+' '
        canvas[self.r+3][self.c+2]=Back.BLACK+' '
        canvas[self.r+3][self.c+3]=Back.BLACK+' '
        canvas[self.r+4][self.c]=Back.BLACK+' '
        canvas[self.r+4][self.c+1]=Back.BLACK+' '
        canvas[self.r+4][self.c+2]=Back.BLACK+' '
        canvas[self.r+4][self.c+3]=Back.BLACK+' '
        if(string=="left" and canvas[self.r+2][self.c-self.speedx-1]==str(Back.BLACK+' ') and canvas[self.r+4][self.c-self.speedx-1]==str(Back.BLACK+' ')):
            self.c= self.c-self.speedx
        elif(string=="right" and canvas[self.r+3][self.c+self.speedx+3]==str(Back.BLACK+' ') and canvas[self.r+2][self.c+self.speedx+3]==str(Back.BLACK+' ') and canvas[self.r+4][self.c+self.speedx+3]==str(Back.BLACK+' ')):
            self.c= self.c+self.speedx
        elif(string=="up" and canvas[self.r-self.speedy+2][self.c-1]==str(Back.BLACK + ' ') and canvas[self.r-self.speedy+2][self.c+3]==str(Back.BLACK + ' ')):
            self.r = self.r-self.speedy
        elif(string=="down" and canvas[self.r+self.speedy+4][self.c-1]==str(Back.BLACK + ' ') and canvas[self.r+self.speedy+4][self.c+3]==str(Back.BLACK + ' ')):
            self.r = self.r+self.speedy

    def attack(self, huts, Townhall, walls,cannons, wizTowers, LMov):
        # checking for walls
        print(LMov)
        if(LMov=="right"):
            for wall in walls:
                if(wall.row<= self.r+6 and wall.row>=self.r and wall.column>=self.c+3 and wall.column<=self.c+11 and wall.health>0):
                    wall.health=wall.health -50
            for hut in huts:
                if(doOverlap(self.r,self.c+3,self.r+6,self.c+11,hut.UpperLeftRow,hut.UpperLeftColumn,hut.LowerRightRow,hut.LowerRightColumn )and hut.health>0):
                    hut.health=hut.health -50
            for cannon in cannons:
                if(doOverlap(self.r,self.c+3,self.r+6,self.c+11,cannon.UpperLeftRow,cannon.UpperLeftColumn,cannon.LowerRightRow,cannon.LowerRightColumn) and cannon.health>0):
                    cannon.health=cannon.health -50
            for wiz in wizTowers:
                if(doOverlap(self.r,self.c+3,self.r+6,self.c+11,wiz.UpperLeftRow,wiz.UpperLeftColumn,wiz.LowerRightRow,wiz.LowerRightColumn) and wiz.health>0):
                    wiz.health=wiz.health -50
            if(doOverlap(self.r,self.c+3,self.r+6,self.c+11,Townhall.UpperLeftRow,Townhall.UpperLeftColumn,Townhall.LowerRightRow,Townhall.LowerRightColumn)and Townhall.health>0):
                Townhall.health = Townhall.health - 50
        elif(LMov=="left"):
            for wall in walls:
                if(wall.row<= self.r+6 and wall.row>=self.r and wall.column>=self.c-8 and wall.column<=self.c and wall.health>0):
                    wall.health=wall.health -50
            for hut in huts:
                if(doOverlap(self.r,self.c-8,self.r+6,self.c,hut.UpperLeftRow,hut.UpperLeftColumn,hut.LowerRightRow,hut.LowerRightColumn )and hut.health>0):
                    hut.health=hut.health -50
            for cannon in cannons:
                if(doOverlap(self.r,self.c-8,self.r+6,self.c,cannon.UpperLeftRow,cannon.UpperLeftColumn,cannon.LowerRightRow,cannon.LowerRightColumn) and cannon.health>0):
                    cannon.health=cannon.health -50
            for wiz in wizTowers:
                if(doOverlap(self.r,self.c-8,self.r+6,self.c,wiz.UpperLeftRow,wiz.UpperLeftColumn,wiz.LowerRightRow,wiz.LowerRightColumn) and wiz.health>0):
                    wiz.health=wiz.health -50
            if(doOverlap(self.r,self.c-8,self.r+6,self.c,Townhall.UpperLeftRow,Townhall.UpperLeftColumn,Townhall.LowerRightRow,Townhall.LowerRightColumn)and Townhall.health>0):
                Townhall.health = Townhall.health - 50
            elif(LMov=="up"):
                for wall in walls:
                    if(wall.row<= self.r+2 and wall.row>=self.r-4 and wall.column>=self.c-3 and wall.column<=self.c+5 and wall.health>0):
                        wall.health=wall.health -50
                for hut in huts:
                    if(doOverlap(self.r-4,self.c-3,self.r+2,self.c+5,hut.UpperLeftRow,hut.UpperLeftColumn,hut.LowerRightRow,hut.LowerRightColumn )and hut.health>0):
                        hut.health=hut.health -50
                for cannon in cannons:
                    if(doOverlap(self.r-4,self.c-3,self.r+2,self.c+5,cannon.UpperLeftRow,cannon.UpperLeftColumn,cannon.LowerRightRow,cannon.LowerRightColumn) and cannon.health>0):
                        cannon.health=cannon.health -50
                for wiz in wizTowers:
                    if(doOverlap(self.r-4,self.c-3,self.r+2,self.c+5,wiz.UpperLeftRow,wiz.UpperLeftColumn,wiz.LowerRightRow,wiz.LowerRightColumn) and wiz.health>0):
                        wiz.health=wiz.health -50
                if(doOverlap(self.r-4,self.c-3,self.r+2,self.c+5,Townhall.UpperLeftRow,Townhall.UpperLeftColumn,Townhall.LowerRightRow,Townhall.LowerRightColumn)and Townhall.health>0):
                    Townhall.health = Townhall.health - 50
            elif(LMov=="down"):
                for wall in walls:
                    if(wall.row<= self.r+10 and wall.row>=self.r+4 and wall.column>=self.c-3 and wall.column<=self.c+5 and wall.health>0):
                        wall.health=wall.health -50
                for hut in huts:
                    if(doOverlap(self.r+4,self.c-3,self.r+10,self.c+5,hut.UpperLeftRow,hut.UpperLeftColumn,hut.LowerRightRow,hut.LowerRightColumn )and hut.health>0):
                        hut.health=hut.health -50
                for cannon in cannons:
                    if(doOverlap(self.r+4,self.c-3,self.r+10,self.c+5,cannon.UpperLeftRow,cannon.UpperLeftColumn,cannon.LowerRightRow,cannon.LowerRightColumn) and cannon.health>0):
                        cannon.health=cannon.health -50
                for wiz in wizTowers:
                    if(doOverlap(self.r+4,self.c-3,self.r+10,self.c+5,wiz.UpperLeftRow,wiz.UpperLeftColumn,wiz.LowerRightRow,wiz.LowerRightColumn) and wiz.health>0):
                        wiz.health=wiz.health -50
                if(doOverlap(self.r+4,self.c-3,self.r+10,self.c+5,Townhall.UpperLeftRow,Townhall.UpperLeftColumn,Townhall.LowerRightRow,Townhall.LowerRightColumn)and Townhall.health>0):
                    Townhall.health = Townhall.health - 50

class Barbs(Troop):
    def __init__(self,x,y):
        Troop.__init__(self,x, y)
        self.health = 100
        self.dpf = 1
        self.existence = 0
        self.mov=0

    
    def display(self, canvas):
        if(self.health>0):
            healthPercent = (self.health)#this has to be changed while changing health
            if(healthPercent>50 and healthPercent<=100 ):
                canvas[self.r][self.c]= Fore.GREEN+'♂'
            if(healthPercent>25 and healthPercent<=50 ):
                canvas[self.r][self.c]= Fore.YELLOW+'♂'
            if(healthPercent>0 and healthPercent<=25 ):
                canvas[self.r][self.c]= Fore.RED+'♂'
        else:
            canvas[self.r][self.c]=Back.BLACK+' '
            self.existence=0
    def getTarget(self,huts, cannons, townhall, wiztowers):
        minHut=huts[0]
        minCannon=cannons[0]
        minWiz=wiztowers[0]
        mindist_hut = 10000
        for hut in huts:
            if(dis(self.r,self.c,hut.cr,hut.cc)<mindist_hut and hut.health>0):
                mindist_hut = dis(self.r,self.c,hut.cr,hut.cc)
                minHut = hut
        mindist_wiz=10000
        for wiz in wiztowers:
            if(dis(self.r,self.c,wiz.cr,wiz.cc)<mindist_wiz and wiz.health>0):
                mindist_wiz = dis(self.r,self.c, wiz.cr,wiz.cc)
                minWiz = wiz
        mindist_cannon=10000
        for cannon in cannons:
            if(dis(self.r,self.c,cannon.cr,cannon.cc)<mindist_cannon and cannon.health>0):
                mindist_cannon = dis(self.r,self.c,cannon.cr,cannon.cc)
                minCannon = cannon
        mindist_townhall=10000
        if(townhall.health>0):
            mindist_townhall =dis(self.r,self.c,townhall.cr,townhall.cc)
        if (mindist_hut <= mindist_cannon and mindist_hut<= mindist_townhall and mindist_hut <= mindist_wiz):
            return minHut
        if (mindist_cannon <= mindist_hut and mindist_cannon<= mindist_townhall and mindist_cannon <= mindist_wiz):
            return minCannon
        if (mindist_townhall <= mindist_cannon and mindist_townhall<= mindist_hut and mindist_townhall <= mindist_wiz):
            return townhall
        if (mindist_wiz <= mindist_cannon and mindist_wiz<= mindist_hut and mindist_wiz <= mindist_townhall):
            return minWiz


    def damage(self,r,c,target,walls,canvas):
        count=0
        for wall in walls:
            
            if (wall.row==r and wall.column==c and wall.health>0):
                wall.health=wall.health-self.dpf
                count=1
        if(count==0):
            target.health = target.health - self.dpf                    



    def update(self, target,canvas,walls):
        canvas[self.r][self.c]= Back.BLACK+' '
        string1= Fore.GREEN+'♂'
        string2= Fore.YELLOW+'♂'
        string3= Fore.RED+'♂'
        string4= Fore.GREEN+'♀'
        string5= Fore.YELLOW+'♀'
        string6= Fore.RED+'♀'
        string7= Fore.GREEN+'o'
        string8= Fore.YELLOW+'o'
        string9= Fore.RED+'o'
        
        if(target.cr==self.r and target.cc > self.c):
            if(canvas[self.r][self.c + self.speedx]==str(Back.BLACK+' ') or canvas[self.r][self.c + self.speedx]==string1 or canvas[self.r][self.c + self.speedx]==string2 or canvas[self.r][self.c + self.speedx]==string3 or canvas[self.r][self.c + self.speedx]==string4 or canvas[self.r][self.c + self.speedx]==string5 or canvas[self.r][self.c + self.speedx]==string6 or canvas[self.r][self.c + self.speedx]==string7 or canvas[self.r][self.c + self.speedx]==string8 or canvas[self.r][self.c + self.speedx]==string9 or canvas[self.r][self.c + self.speedx]==str(Fore.GREEN+'1') or canvas[self.r][self.c + self.speedx]==str(Fore.GREEN+'2') or canvas[self.r][self.c + self.speedx]==str(Fore.GREEN+'3')):
                self.c = self.c + self.speedx
            else:
                self.damage(self.r,self.c + self.speedx,target,walls,canvas)
        elif(target.cr==self.r and target.cc < self.c):
            if(canvas[self.r][self.c - self.speedx]==str(Back.BLACK+' ') or canvas[self.r][self.c - self.speedx]==string1 or canvas[self.r][self.c - self.speedx]==string2 or canvas[self.r][self.c - self.speedx]==string3 or canvas[self.r][self.c - self.speedx]==string4 or canvas[self.r][self.c - self.speedx]==string5 or canvas[self.r][self.c - self.speedx]==string6 or canvas[self.r][self.c - self.speedx]==string7 or canvas[self.r][self.c - self.speedx]==string8 or canvas[self.r][self.c - self.speedx]==string9 or canvas[self.r][self.c - self.speedx]==str(Fore.GREEN+'1') or canvas[self.r][self.c - self.speedx]==str(Fore.GREEN+'2') or canvas[self.r][self.c - self.speedx]==str(Fore.GREEN+'3')):
                self.c = self.c - self.speedx
            else:
                self.damage(self.r,self.c - self.speedx,target,walls,canvas)
        elif(target.cc==self.c and target.cr < self.r):
            if(canvas[self.r - self.speedy][self.c]==str(Back.BLACK+' ') or canvas[self.r - self.speedy][self.c]==string1 or canvas[self.r - self.speedy][self.c]==string2 or canvas[self.r - self.speedy][self.c]==string3 or canvas[self.r - self.speedy][self.c]==string4 or canvas[self.r - self.speedy][self.c]==string5 or canvas[self.r - self.speedy][self.c]==string6 or canvas[self.r - self.speedy][self.c]==string7 or canvas[self.r - self.speedy][self.c]==string8 or canvas[self.r - self.speedy][self.c]==string9 or canvas[self.r - self.speedy][self.c]==str(Fore.GREEN+'1') or canvas[self.r - self.speedy][self.c]==str(Fore.GREEN+'2') or canvas[self.r - self.speedy][self.c]==str(Fore.GREEN+'3')):
                self.r = self.r - self.speedy
            else:
                self.damage(self.r - self.speedy,self.c,target,walls,canvas)
        elif(target.cc==self.c and target.cr > self.r):
            if(canvas[self.r + self.speedy][self.c]==str(Back.BLACK+' ') or canvas[self.r + self.speedy][self.c]==string1 or canvas[self.r + self.speedy][self.c]==string2 or canvas[self.r + self.speedy][self.c]==string3 or canvas[self.r + self.speedy][self.c]==string4 or canvas[self.r + self.speedy][self.c]==string5 or canvas[self.r + self.speedy][self.c]==string6 or canvas[self.r + self.speedy][self.c]==string7 or canvas[self.r + self.speedy][self.c]==string8 or canvas[self.r + self.speedy][self.c]==string9 or canvas[self.r + self.speedy][self.c]==str(Fore.GREEN+'1') or canvas[self.r + self.speedy][self.c]==str(Fore.GREEN+'2') or canvas[self.r + self.speedy][self.c]==str(Fore.GREEN+'3')):
                self.r = self.r + self.speedy
            else:
                self.damage(self.r + self.speedy,self.c,target,walls,canvas)
        elif(target.cc>self.c and target.cr > self.r):
            if(canvas[self.r + self.speedy][self.c + self.speedx]==str(Back.BLACK+' ')or canvas[self.r + self.speedy][self.c + self.speedx]==string1 or canvas[self.r + self.speedy][self.c + self.speedx]==string2 or canvas[self.r + self.speedy][self.c + self.speedx]==string3 or canvas[self.r + self.speedy][self.c + self.speedx]==string4 or canvas[self.r + self.speedy][self.c + self.speedx]==string5 or canvas[self.r + self.speedy][self.c + self.speedx]==string6 or canvas[self.r + self.speedy][self.c + self.speedx]==string7 or canvas[self.r + self.speedy][self.c + self.speedx]==string8 or canvas[self.r + self.speedy][self.c + self.speedx]==string9 or canvas[self.r + self.speedy][self.c + self.speedx]==str(Fore.GREEN+'1') or canvas[self.r + self.speedy][self.c + self.speedx]==str(Fore.GREEN+'2') or canvas[self.r + self.speedy][self.c + self.speedx]==str(Fore.GREEN+'3')): 
                self.r = self.r + self.speedy
                self.c = self.c + self.speedx
            else:
                self.damage(self.r + self.speedy,self.c + self.speedx,target,walls,canvas)
            
        elif(target.cc>self.c and target.cr < self.r):
            if(canvas[self.r - self.speedy][self.c + self.speedx]==str(Back.BLACK+' ')or canvas[self.r - self.speedy][self.c + self.speedx]==string1 or canvas[self.r - self.speedy][self.c + self.speedx]==string2 or canvas[self.r - self.speedy][self.c + self.speedx]==string3 or canvas[self.r - self.speedy][self.c + self.speedx]==string4 or canvas[self.r - self.speedy][self.c + self.speedx]==string5 or canvas[self.r - self.speedy][self.c + self.speedx]==string6 or canvas[self.r - self.speedy][self.c + self.speedx]==string7 or canvas[self.r - self.speedy][self.c + self.speedx]==string8 or canvas[self.r - self.speedy][self.c + self.speedx]==string9 or canvas[self.r - self.speedy][self.c + self.speedx]==str(Fore.GREEN+'1') or canvas[self.r - self.speedy][self.c + self.speedx]==str(Fore.GREEN+'2') or canvas[self.r - self.speedy][self.c + self.speedx]==str(Fore.GREEN+'3')):
                self.r = self.r - self.speedy
                self.c = self.c + self.speedx
            else:
                self.damage(self.r - self.speedy,self.c + self.speedx,target,walls,canvas)
        elif(target.cc<self.c and target.cr > self.r):
            if(canvas[self.r + self.speedy][self.c - self.speedx]==str(Back.BLACK+' ')or canvas[self.r + self.speedy][self.c - self.speedx]==string1 or canvas[self.r + self.speedy][self.c - self.speedx]==string2 or canvas[self.r + self.speedy][self.c - self.speedx]==string3 or canvas[self.r + self.speedy][self.c - self.speedx]==string4 or canvas[self.r + self.speedy][self.c - self.speedx]==string5 or canvas[self.r + self.speedy][self.c - self.speedx]==string6 or canvas[self.r + self.speedy][self.c - self.speedx]==string7 or canvas[self.r + self.speedy][self.c - self.speedx]==string8 or canvas[self.r + self.speedy][self.c - self.speedx]==string9 or canvas[self.r + self.speedy][self.c - self.speedx]==str(Fore.GREEN+'1') or canvas[self.r + self.speedy][self.c - self.speedx]==str(Fore.GREEN+'2') or canvas[self.r + self.speedy][self.c - self.speedx]==str(Fore.GREEN+'3')):
                self.r = self.r + self.speedy
                self.c = self.c - self.speedx
            else:
                self.damage(self.r + self.speedy,self.c - self.speedx,target,walls,canvas)
        elif(target.cc<self.c and target.cr < self.r):
            if(canvas[self.r - self.speedy][self.c - self.speedx]==str(Back.BLACK+' ')or canvas[self.r - self.speedy][self.c - self.speedx]==string1 or canvas[self.r - self.speedy][self.c - self.speedx]==string2 or canvas[self.r - self.speedy][self.c - self.speedx]==string3 or canvas[self.r - self.speedy][self.c - self.speedx]==string4 or canvas[self.r - self.speedy][self.c - self.speedx]==string5 or canvas[self.r - self.speedy][self.c - self.speedx]==string6 or canvas[self.r - self.speedy][self.c - self.speedx]==string7 or canvas[self.r - self.speedy][self.c - self.speedx]==string8 or canvas[self.r - self.speedy][self.c - self.speedx]==string9 or canvas[self.r - self.speedy][self.c - self.speedx]==str(Fore.GREEN+'1') or canvas[self.r - self.speedy][self.c - self.speedx]==str(Fore.GREEN+'2') or canvas[self.r - self.speedy][self.c - self.speedx]==str(Fore.GREEN+'3')):
                self.r = self.r - self.speedy
                self.c = self.c - self.speedx
            else:
                self.damage(self.r - self.speedy,self.c - self.speedx,target,walls,canvas)
        

        
class Archers(Troop):
    def __init__(self,x, y):
        Troop.__init__(self,x,y)
        self.health = 50
        self.dpf = 0.5
        self.existence = 0
        self.attackRange = 25

    def display(self, canvas):
        if(self.health>0):
            healthPercent = self.health*2 #this has to be changed while changing health
            if(healthPercent>50 and healthPercent<=100 ):
                canvas[self.r][self.c]= Fore.GREEN+'♀'
            if(healthPercent>25 and healthPercent<=50 ):
                canvas[self.r][self.c]= Fore.YELLOW+'♀'
            if(healthPercent>0 and healthPercent<=25 ):
                canvas[self.r][self.c]= Fore.RED+'♀'
        else:
            canvas[self.r][self.c]=Back.BLACK+' '
            self.existence=0

    def getTargetWithinRange(self,huts, cannons, townhall, wiztowers):
        minHut=huts[0]
        minCannon=cannons[0]
        minWiz=wiztowers[0]
        mindist_hut = 10000
        for hut in huts:
            if(dis(self.r,self.c,hut.cr,hut.cc)<mindist_hut and hut.health>0 and dis(self.r,self.c,hut.cr,hut.cc)< self.attackRange):
                mindist_hut = dis(self.r,self.c,hut.cr,hut.cc)
                minHut = hut
        mindist_wiz=10000
        for wiz in wiztowers:
            if(dis(self.r,self.c,wiz.cr,wiz.cc)<mindist_wiz and wiz.health>0 and dis(self.r,self.c,wiz.cr,wiz.cc)< self.attackRange):
                mindist_wiz = dis(self.r,self.c, wiz.cr,wiz.cc)
                minWiz = wiz
        mindist_cannon=10000
        for cannon in cannons:
            if(dis(self.r,self.c,cannon.cr,cannon.cc)<mindist_cannon and cannon.health>0 and dis(self.r,self.c,cannon.cr,cannon.cc)< self.attackRange):
                mindist_cannon = dis(self.r,self.c,cannon.cr,cannon.cc)
                minCannon = cannon
        mindist_townhall=10000
        if(townhall.health>0 and dis(self.r,self.c,townhall.cr,townhall.cc)< self.attackRange):
            mindist_townhall =dis(self.r,self.c,townhall.cr,townhall.cc)
        if (mindist_hut <= mindist_cannon and mindist_hut<= mindist_townhall and mindist_hut <= mindist_wiz and mindist_hut !=10000 ):
            return minHut
        elif (mindist_cannon <= mindist_hut and mindist_cannon<= mindist_townhall and mindist_cannon <= mindist_wiz and mindist_cannon != 10000):
            return minCannon
        elif (mindist_townhall <= mindist_cannon and mindist_townhall<= mindist_hut and mindist_townhall <= mindist_wiz and mindist_townhall!=10000):
            return townhall
        elif (mindist_wiz <= mindist_cannon and mindist_wiz<= mindist_hut and mindist_wiz <= mindist_townhall and mindist_wiz!=10000):
            return minWiz
        else:
            return -1

    def getTarget(self,huts, cannons, townhall, wiztowers):
        minHut=huts[0]
        minCannon=cannons[0]
        minWiz=wiztowers[0]
        mindist_hut = 10000
        for hut in huts:
            if(dis(self.r,self.c,hut.cr,hut.cc)<mindist_hut and hut.health>0):
                mindist_hut = dis(self.r,self.c,hut.cr,hut.cc)
                minHut = hut
        mindist_wiz=10000
        for wiz in wiztowers:
            if(dis(self.r,self.c,wiz.cr,wiz.cc)<mindist_wiz and wiz.health>0):
                mindist_wiz = dis(self.r,self.c, wiz.cr,wiz.cc)
                minWiz = wiz
        mindist_cannon=10000
        for cannon in cannons:
            if(dis(self.r,self.c,cannon.cr,cannon.cc)<mindist_cannon and cannon.health>0):
                mindist_cannon = dis(self.r,self.c,cannon.cr,cannon.cc)
                minCannon = cannon
        mindist_townhall=10000
        if(townhall.health>0):
            mindist_townhall =dis(self.r,self.c,townhall.cr,townhall.cc)
        if (mindist_hut <= mindist_cannon and mindist_hut<= mindist_townhall and mindist_hut <= mindist_wiz):
            return minHut
        if (mindist_cannon <= mindist_hut and mindist_cannon<= mindist_townhall and mindist_cannon <= mindist_wiz):
            return minCannon
        if (mindist_townhall <= mindist_cannon and mindist_townhall<= mindist_hut and mindist_townhall <= mindist_wiz):
            return townhall
        if (mindist_wiz <= mindist_cannon and mindist_wiz<= mindist_hut and mindist_wiz <= mindist_townhall):
            return minWiz



    def Damage(self,target):
        target.health = target.health - self.dpf

    def damage(self,r,c,target,walls,canvas):
        for wall in walls:
            
            if (wall.row==r and wall.column==c and wall.health>0):
                wall.health=wall.health-self.dpf
                count=1
                            

    def update(self, target,canvas,walls):
        canvas[self.r][self.c]= Back.BLACK+' '
        string1= Fore.GREEN+'♂'
        string2= Fore.YELLOW+'♂'
        string3= Fore.RED+'♂'
        string4= Fore.GREEN+'♀'
        string5= Fore.YELLOW+'♀'
        string6= Fore.RED+'♀'
        string7= Fore.GREEN+'o'
        string8= Fore.YELLOW+'o'
        string9= Fore.RED+'o'
        
        if(target.cr==self.r and target.cc > self.c):
            if(canvas[self.r][self.c + self.speedx]==str(Back.BLACK+' ') or canvas[self.r][self.c + self.speedx]==string1 or canvas[self.r][self.c + self.speedx]==string2 or canvas[self.r][self.c + self.speedx]==string3 or canvas[self.r][self.c + self.speedx]==string4 or canvas[self.r][self.c + self.speedx]==string5 or canvas[self.r][self.c + self.speedx]==string6 or canvas[self.r][self.c + self.speedx]==string7 or canvas[self.r][self.c + self.speedx]==string8 or canvas[self.r][self.c + self.speedx]==string9 or canvas[self.r][self.c + self.speedx]==str(Fore.GREEN+'1') or canvas[self.r][self.c + self.speedx]==str(Fore.GREEN+'2') or canvas[self.r][self.c + self.speedx]==str(Fore.GREEN+'3')):
                self.c = self.c + self.speedx
            else:
                self.damage(self.r,self.c + self.speedx,target,walls,canvas)
        elif(target.cr==self.r and target.cc < self.c):
            if(canvas[self.r][self.c - self.speedx]==str(Back.BLACK+' ') or canvas[self.r][self.c - self.speedx]==string1 or canvas[self.r][self.c - self.speedx]==string2 or canvas[self.r][self.c - self.speedx]==string3 or canvas[self.r][self.c - self.speedx]==string4 or canvas[self.r][self.c - self.speedx]==string5 or canvas[self.r][self.c - self.speedx]==string6 or canvas[self.r][self.c - self.speedx]==string7 or canvas[self.r][self.c - self.speedx]==string8 or canvas[self.r][self.c - self.speedx]==string9 or canvas[self.r][self.c - self.speedx]==str(Fore.GREEN+'1') or canvas[self.r][self.c - self.speedx]==str(Fore.GREEN+'2') or canvas[self.r][self.c - self.speedx]==str(Fore.GREEN+'3')):
                self.c = self.c - self.speedx
            else:
                self.damage(self.r,self.c - self.speedx,target,walls,canvas)
        elif(target.cc==self.c and target.cr < self.r):
            if(canvas[self.r - self.speedy][self.c]==str(Back.BLACK+' ') or canvas[self.r - self.speedy][self.c]==string1 or canvas[self.r - self.speedy][self.c]==string2 or canvas[self.r - self.speedy][self.c]==string3 or canvas[self.r - self.speedy][self.c]==string4 or canvas[self.r - self.speedy][self.c]==string5 or canvas[self.r - self.speedy][self.c]==string6 or canvas[self.r - self.speedy][self.c]==string7 or canvas[self.r - self.speedy][self.c]==string8 or canvas[self.r - self.speedy][self.c]==string9 or canvas[self.r - self.speedy][self.c]==str(Fore.GREEN+'1') or canvas[self.r - self.speedy][self.c]==str(Fore.GREEN+'2') or canvas[self.r - self.speedy][self.c]==str(Fore.GREEN+'3')):
                self.r = self.r - self.speedy
            else:
                self.damage(self.r - self.speedy,self.c,target,walls,canvas)
        elif(target.cc==self.c and target.cr > self.r):
            if(canvas[self.r + self.speedy][self.c]==str(Back.BLACK+' ') or canvas[self.r + self.speedy][self.c]==string1 or canvas[self.r + self.speedy][self.c]==string2 or canvas[self.r + self.speedy][self.c]==string3 or canvas[self.r + self.speedy][self.c]==string4 or canvas[self.r + self.speedy][self.c]==string5 or canvas[self.r + self.speedy][self.c]==string6 or canvas[self.r + self.speedy][self.c]==string7 or canvas[self.r + self.speedy][self.c]==string8 or canvas[self.r + self.speedy][self.c]==string9 or canvas[self.r + self.speedy][self.c]==str(Fore.GREEN+'1') or canvas[self.r + self.speedy][self.c]==str(Fore.GREEN+'2') or canvas[self.r + self.speedy][self.c]==str(Fore.GREEN+'3')):
                self.r = self.r + self.speedy
            else:
                self.damage(self.r + self.speedy,self.c,target,walls,canvas)
        elif(target.cc>self.c and target.cr > self.r):
            if(canvas[self.r + self.speedy][self.c + self.speedx]==str(Back.BLACK+' ')or canvas[self.r + self.speedy][self.c + self.speedx]==string1 or canvas[self.r + self.speedy][self.c + self.speedx]==string2 or canvas[self.r + self.speedy][self.c + self.speedx]==string3 or canvas[self.r + self.speedy][self.c + self.speedx]==string4 or canvas[self.r + self.speedy][self.c + self.speedx]==string5 or canvas[self.r + self.speedy][self.c + self.speedx]==string6 or canvas[self.r + self.speedy][self.c + self.speedx]==string7 or canvas[self.r + self.speedy][self.c + self.speedx]==string8 or canvas[self.r + self.speedy][self.c + self.speedx]==string9 or canvas[self.r + self.speedy][self.c + self.speedx]==str(Fore.GREEN+'1') or canvas[self.r + self.speedy][self.c + self.speedx]==str(Fore.GREEN+'2') or canvas[self.r + self.speedy][self.c + self.speedx]==str(Fore.GREEN+'3')): 
                self.r = self.r + self.speedy
                self.c = self.c + self.speedx
            else:
                self.damage(self.r + self.speedy,self.c + self.speedx,target,walls,canvas)
            
        elif(target.cc>self.c and target.cr < self.r):
            if(canvas[self.r - self.speedy][self.c + self.speedx]==str(Back.BLACK+' ')or canvas[self.r - self.speedy][self.c + self.speedx]==string1 or canvas[self.r - self.speedy][self.c + self.speedx]==string2 or canvas[self.r - self.speedy][self.c + self.speedx]==string3 or canvas[self.r - self.speedy][self.c + self.speedx]==string4 or canvas[self.r - self.speedy][self.c + self.speedx]==string5 or canvas[self.r - self.speedy][self.c + self.speedx]==string6 or canvas[self.r - self.speedy][self.c + self.speedx]==string7 or canvas[self.r - self.speedy][self.c + self.speedx]==string8 or canvas[self.r - self.speedy][self.c + self.speedx]==string9 or canvas[self.r - self.speedy][self.c + self.speedx]==str(Fore.GREEN+'1') or canvas[self.r - self.speedy][self.c + self.speedx]==str(Fore.GREEN+'2') or canvas[self.r - self.speedy][self.c + self.speedx]==str(Fore.GREEN+'3')):
                self.r = self.r - self.speedy
                self.c = self.c + self.speedx
            else:
                self.damage(self.r - self.speedy,self.c + self.speedx,target,walls,canvas)
        elif(target.cc<self.c and target.cr > self.r):
            if(canvas[self.r + self.speedy][self.c - self.speedx]==str(Back.BLACK+' ')or canvas[self.r + self.speedy][self.c - self.speedx]==string1 or canvas[self.r + self.speedy][self.c - self.speedx]==string2 or canvas[self.r + self.speedy][self.c - self.speedx]==string3 or canvas[self.r + self.speedy][self.c - self.speedx]==string4 or canvas[self.r + self.speedy][self.c - self.speedx]==string5 or canvas[self.r + self.speedy][self.c - self.speedx]==string6 or canvas[self.r + self.speedy][self.c - self.speedx]==string7 or canvas[self.r + self.speedy][self.c - self.speedx]==string8 or canvas[self.r + self.speedy][self.c - self.speedx]==string9 or canvas[self.r + self.speedy][self.c - self.speedx]==str(Fore.GREEN+'1') or canvas[self.r + self.speedy][self.c - self.speedx]==str(Fore.GREEN+'2') or canvas[self.r + self.speedy][self.c - self.speedx]==str(Fore.GREEN+'3')):
                self.r = self.r + self.speedy
                self.c = self.c - self.speedx
            else:
                self.damage(self.r + self.speedy,self.c - self.speedx,target,walls,canvas)
        elif(target.cc<self.c and target.cr < self.r):
            if(canvas[self.r - self.speedy][self.c - self.speedx]==str(Back.BLACK+' ')or canvas[self.r - self.speedy][self.c - self.speedx]==string1 or canvas[self.r - self.speedy][self.c - self.speedx]==string2 or canvas[self.r - self.speedy][self.c - self.speedx]==string3 or canvas[self.r - self.speedy][self.c - self.speedx]==string4 or canvas[self.r - self.speedy][self.c - self.speedx]==string5 or canvas[self.r - self.speedy][self.c - self.speedx]==string6 or canvas[self.r - self.speedy][self.c - self.speedx]==string7 or canvas[self.r - self.speedy][self.c - self.speedx]==string8 or canvas[self.r - self.speedy][self.c - self.speedx]==string9 or canvas[self.r - self.speedy][self.c - self.speedx]==str(Fore.GREEN+'1') or canvas[self.r - self.speedy][self.c - self.speedx]==str(Fore.GREEN+'2') or canvas[self.r - self.speedy][self.c - self.speedx]==str(Fore.GREEN+'3')):
                self.r = self.r - self.speedy
                self.c = self.c - self.speedx
            else:
                self.damage(self.r - self.speedy,self.c - self.speedx,target,walls,canvas)


class Balloons(Troop):
    def __init__(self,x, y):
        Troop.__init__(self,x,y)
        self.health = 100
        self.dpf = 2
        self.existence = 0
        

    def display(self, canvas):
        if(self.health>0):
            healthPercent = (self.health) #this has to be changed while changing health
            if(healthPercent>50 and healthPercent<=100 ):
                canvas[self.r][self.c]= Fore.GREEN+'o'
            if(healthPercent>25 and healthPercent<=50 ):
                canvas[self.r][self.c]= Fore.YELLOW+'o'
            if(healthPercent>0 and healthPercent<=25 ):
                canvas[self.r][self.c]= Fore.RED+'o'
        else:
            canvas[self.r][self.c]=Back.BLACK+' '
            self.existence=0

    def getTarget(self,huts, cannons, townhall, wiztowers):
        count=0
        for i in cannons:
            if i.health <=0:
                count+=1
        for i in wiztowers:
            if i.health <=0:
                count+=1
        
        if count == len(cannons)+len(wiztowers):
            minHut=huts[0]
            mindist_hut = 10000
            for hut in huts:
                if(dis(self.r,self.c,hut.cr,hut.cc)<mindist_hut and hut.health>0):
                    mindist_hut = dis(self.r,self.c,hut.cr,hut.cc)
                    minHut = hut
            mindist_townhall=10000
            if(townhall.health>0):
                mindist_townhall =dis(self.r,self.c,townhall.cr,townhall.cc)
            if(mindist_hut<= mindist_townhall):
                return minHut
            else:
                return townhall
        else:
            minCannon=cannons[0]
            minWiz=wiztowers[0]
            
            mindist_wiz=10000
            for wiz in wiztowers:
                if(dis(self.r,self.c,wiz.cr,wiz.cc)<mindist_wiz and wiz.health>0):
                    mindist_wiz = dis(self.r,self.c, wiz.cr,wiz.cc)
                    minWiz = wiz
            mindist_cannon=10000
            for cannon in cannons:
                if(dis(self.r,self.c,cannon.cr,cannon.cc)<mindist_cannon and cannon.health>0):
                    mindist_cannon = dis(self.r,self.c,cannon.cr,cannon.cc)
                    minCannon = cannon
            if (mindist_wiz <= mindist_cannon):
                return minWiz
            else:
                return minCannon

        
        
    def update(self, target,canvas,walls):
        canvas[self.r][self.c]= Back.BLACK+' '
        
        if(target.cr==self.r and target.cc > self.c  and ((self.r<target.cr-2  or self.r>target.cr+2 ) or (self.c<target.cc-2  or self.c>target.cc+2))):
            self.c = self.c + self.speedx
        elif(target.cr==self.r and target.cc < self.c and(( self.r<target.cr-2 or  self.r>target.cr+2) or ( self.c<target.cc-2 or  self.c>target.cc+2))):
            self.c = self.c - self.speedx
        elif(target.cc==self.c and target.cr < self.r and(( self.r<target.cr-2 or  self.r>target.cr+2) or ( self.c<target.cc-2 or  self.c>target.cc+2))):
            self.r = self.r - self.speedy
        elif(target.cc==self.c and target.cr > self.r and(( self.r<target.cr-2 or  self.r>target.cr+2) or ( self.c<target.cc-2 or  self.c>target.cc+2))):
            self.r = self.r + self.speedy
        elif(target.cc>self.c and target.cr > self.r and ((self.r<target.cr-2  or self.r>target.cr+2 ) or (self.c<target.cc-2  or self.c>target.cc+2))):
            self.r = self.r + self.speedy
            self.c = self.c + self.speedx
            
        elif(target.cc>self.c and target.cr < self.r and ((self.r<target.cr-2  or self.r>target.cr+2 ) or (self.c<target.cc-2  or self.c>target.cc+2))):
            self.r = self.r - self.speedy
            self.c = self.c + self.speedx
        elif(target.cc<self.c and target.cr > self.r and ((self.r<target.cr-2  or self.r>target.cr+2 ) or (self.c<target.cc-2  or self.c>target.cc+2))):
            self.r = self.r + self.speedy
            self.c = self.c - self.speedx
        elif(target.cc<self.c and target.cr < self.r and ((self.r<target.cr-2  or self.r>target.cr+2 ) or (self.c<target.cc-2  or self.c>target.cc+2))):
            self.r = self.r - self.speedy
            self.c = self.c - self.speedx
        else:
            target.health = target.health - self.dpf





