import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import numpy as np

def dis(x1,y1,x2,y2):
    return(np.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))

class Building:
    def __init__(self,ur,uc,lr,lc):
        self.UpperLeftRow = ur
        self.UpperLeftColumn = uc
        self.UpperRightRow = ur
        self.UpperRightColumn = lc
        self.LowerLeftRow = lr
        self.LowerLeftColumn = uc
        self.LowerRightRow = lr
        self.LowerRightColumn = lc
        self.Width= lc-1 -(uc+1)
        self.Length= lr-1 -(ur+1)
        self.healthPercent=100
        self.cr = (ur+lr)/2
        self.cc = (uc+lc)/2


    def addBuilding(self,canvas):
        if(self.healthPercent>0):
            canvas[self.UpperLeftRow][self.UpperLeftColumn]=Fore.MAGENTA+Style.BRIGHT+Back.LIGHTBLACK_EX+"╔"
            canvas[self.UpperRightRow][self.UpperRightColumn]=Fore.MAGENTA+Style.BRIGHT+Back.LIGHTBLACK_EX+"╗"
            canvas[self.LowerLeftRow][self.LowerLeftColumn]=Fore.MAGENTA+Style.BRIGHT+Back.LIGHTBLACK_EX+"╚"
            canvas[self.LowerRightRow][self.LowerRightColumn]=Fore.MAGENTA+Style.BRIGHT+Back.LIGHTBLACK_EX+"╝"
            for i in range(self.UpperLeftRow+1,self.LowerLeftRow):
                canvas[i][self.UpperLeftColumn]=Fore.MAGENTA+Style.BRIGHT+Back.LIGHTBLACK_EX+'|'
                canvas[i][self.LowerRightColumn]=Fore.MAGENTA+Style.BRIGHT+Back.LIGHTBLACK_EX+'|'
                
            for j in range(self.UpperLeftColumn+1,self.UpperRightColumn):
                canvas[self.UpperLeftRow][j]= Fore.MAGENTA+Style.BRIGHT+Back.LIGHTBLACK_EX+'-'
                canvas[self.LowerRightRow][j]= Fore.MAGENTA+Style.BRIGHT+Back.LIGHTBLACK_EX+'-'
            for i in range(self.UpperLeftColumn+1,self.UpperRightColumn):
                if(self.healthPercent>=50 and self.healthPercent<=100 ):
                    if(i<= self.UpperLeftColumn+1+int(self.healthPercent*self.Width/100)):
                        canvas[self.UpperLeftRow+1][i]= Back.GREEN+' '
                    else:
                        canvas[self.UpperLeftRow+1][i]= Back.BLACK+' '
                if(self.healthPercent>=20 and self.healthPercent<50 ):
                    if(i<= self.UpperLeftColumn+1+int(self.healthPercent*self.Width/100)):
                        canvas[self.UpperLeftRow+1][i]= Back.YELLOW+' '
                    else:
                        canvas[self.UpperLeftRow+1][i]= Back.BLACK+' '
                if(self.healthPercent>0 and self.healthPercent<20 ):
                    if(i<= self.UpperLeftColumn+1+int(self.healthPercent*self.Width/100)):
                        canvas[self.UpperLeftRow+1][i]= Back.RED+' '
                    else:
                        canvas[self.UpperLeftRow+1][i]= Back.BLACK+' '
        else:
            self.RemoveBuilding(canvas)
    def RemoveBuilding(self,canvas):
        if(self.healthPercent>0):
            canvas[self.UpperLeftRow][self.UpperLeftColumn]=Back.BLACK+" "
            canvas[self.UpperRightRow][self.UpperRightColumn]=Back.BLACK+" "
            canvas[self.LowerLeftRow][self.LowerLeftColumn]=Back.BLACK+" "
            canvas[self.LowerRightRow][self.LowerRightColumn]=Back.BLACK+" "
            for i in range(self.UpperLeftRow+1,self.LowerLeftRow):
                canvas[i][self.UpperLeftColumn]=Back.BLACK+' '
                canvas[i][self.LowerRightColumn]=Back.BLACK+' '
                
            for j in range(self.UpperLeftColumn+1,self.UpperRightColumn):
                canvas[self.UpperLeftRow][j]= Back.BLACK+' '
                canvas[self.LowerRightRow][j]= Back.BLACK+' '
            for i in range(self.UpperLeftColumn+1,self.UpperRightColumn):
                        canvas[self.UpperLeftRow+1][i]= Back.BLACK+' '


            

class TownHall(Building):
    def __init__(self):
        Building.__init__(self,15,75,30,115)
        self.health = 500
    def AddTownhall(self,canvas):
        if(self.health>0):
            self.healthPercent = (self.health/500)*100
            Building.addBuilding(self,canvas)
            for i in range(20,30):
                for j in range(77, 114):
                    if(j%3==0):
                        canvas[i][j]=Back.YELLOW + Fore.BLUE+ '⚕'
                    else:
                        canvas[i][j]=Back.YELLOW + Fore.BLUE+ ' '

            for i in range(22,30):
                for j in range(89, 101):
                    canvas[i][j]=Back.LIGHTRED_EX + '|'
            for i in range(18,20):
                for j in range(80, 110):    
                    canvas[i][j]=Back.YELLOW + Fore.WHITE+ '_'
                    
            for j in range(80,110,2):
                    canvas[17][j]=Fore.RED+Back.BLACK+ '♚'
        else:
            Building.RemoveBuilding(self,canvas)
            for i in range(20,30):
                for j in range(77, 114):
                    if(j%3==0):
                        canvas[i][j]=Back.BLACK+ ' '
                    else:
                        canvas[i][j]=Back.BLACK+ ' '

            for i in range(22,30):
                for j in range(89, 101):
                    canvas[i][j]=Back.BLACK + ' '
            for i in range(18,20):
                for j in range(80, 110):    
                    canvas[i][j]=Back.BLACK+ ' '
                    
            for j in range(80,110,2):
                    canvas[17][j]=Back.BLACK+ ' '




    
class Hut(Building):
    def __init__(self,ur,uc,lr,lc):
        Building.__init__(self,ur,uc,lr,lc)
        self.health = 200

    def AddHut(self,canvas):
        if(self.health>0):
            self.healthPercent = (self.health/200)*100
            Building.addBuilding(self,canvas)
            for i in range(self.LowerLeftColumn+2,self.LowerRightColumn-1):
                canvas[self.LowerLeftRow-1][i]=Back.BLUE+'_'
                # canvas[self.LowerLeftRow-2][i]=Back.BLUE+' '
                if(i>=self.LowerLeftColumn+3 and i<=self.LowerRightColumn-3):
                    canvas[self.LowerLeftRow-2][i]=Back.BLUE+'_'
                    if(i>=self.LowerLeftColumn+4 and i<=self.LowerRightColumn-4):
                        canvas[self.LowerLeftRow-3][i]=Back.BLUE+'_'
                        if(i>=self.LowerLeftColumn+5 and i<=self.LowerRightColumn-5):
                            canvas[self.LowerLeftRow-4][i]=Back.BLUE+'_'
                            if(i>=self.LowerLeftColumn+6 and i<=self.LowerRightColumn-6):
                                canvas[self.LowerLeftRow-5][i]=Back.BLUE+'_'
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+10]=Back.BLACK+Fore.YELLOW+'⚑'
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+6]=Back.BLACK+Fore.YELLOW+'⚑'
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+14]=Back.BLACK+Fore.YELLOW+'⚑'
        else:
            Building.RemoveBuilding(self,canvas)
            for i in range(self.LowerLeftColumn+2,self.LowerRightColumn-1):
                canvas[self.LowerLeftRow-1][i]=Back.BLACK+' '
                if(i>=self.LowerLeftColumn+3 and i<=self.LowerRightColumn-3):
                    canvas[self.LowerLeftRow-2][i]=Back.BLACK+' '
                    if(i>=self.LowerLeftColumn+4 and i<=self.LowerRightColumn-4):
                        canvas[self.LowerLeftRow-3][i]=Back.BLACK+' '
                        if(i>=self.LowerLeftColumn+5 and i<=self.LowerRightColumn-5):
                            canvas[self.LowerLeftRow-4][i]=Back.BLACK+' '
                            if(i>=self.LowerLeftColumn+6 and i<=self.LowerRightColumn-6):
                                canvas[self.LowerLeftRow-5][i]=Back.BLACK+' '
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+10]=Back.BLACK+' '
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+6]=Back.BLACK+' '
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+14]=Back.BLACK+' '



class Cannon(Building):
    def __init__(self,ur,uc,lr,lc):
        Building.__init__(self,ur,uc,lr,lc)
        self.health = 350
        self.damage = 2
        self.range= 26

    def AddCannon(self,canvas):
        if(self.health>0):
            self.healthPercent=(self.health/350)*100
            Building.addBuilding(self,canvas)
            # text=f"{Fore.RED}C{Fore.YELLOW}A{Fore.GREEN}N{Fore.BLUE}N{Fore.MAGENTA}O{Fore.WHITE}N"
            text=[]
            text.append(Fore.RED+Back.BLACK+Style.BRIGHT+'C')
            text.append(Fore.YELLOW+Back.BLACK+Style.BRIGHT+'A')
            text.append(Fore.GREEN+Back.BLACK+Style.BRIGHT+'N')
            text.append(Fore.BLUE+Back.BLACK+Style.BRIGHT+'N')
            text.append(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'O')
            text.append(Fore.WHITE+Back.BLACK+Style.BRIGHT+'N')
            
            c=0
            for j in range(self.LowerLeftColumn+1,self.LowerLeftColumn+14):
                if(j%2==0 and c<6):
                    canvas[self.UpperLeftRow+2][j]=text[c]
                    c=c+1
            canvas[self.UpperLeftRow+2][self.LowerLeftColumn+13]=Back.BLACK+'☀'

            for i in range(self.LowerLeftColumn+2,self.LowerLeftColumn+9):
                canvas[self.LowerLeftRow-1][i]=Back.LIGHTBLACK_EX+Fore.BLACK+'_'
            for i in range(self.LowerLeftColumn+3,self.LowerLeftColumn+8):
                if(i%5==0):
                    canvas[self.LowerLeftRow-2][i]=Back.LIGHTBLACK_EX+Fore.WHITE+'☠'
                else:
                    canvas[self.LowerLeftRow-2][i]=Back.LIGHTBLACK_EX+' '
            for i in range(self.LowerLeftRow-4,self.LowerLeftRow-2):
                for j in range(self.LowerLeftColumn+1,self.LowerLeftColumn+14):
                    if(j%3==0):
                        canvas[i][j]=Back.LIGHTBLACK_EX+Fore.BLACK+'☷'
                    else:
                        canvas[i][j]=Back.LIGHTBLACK_EX+' '
        else:
            c=0
            Building.RemoveBuilding(self,canvas)
            for j in range(self.LowerLeftColumn+1,self.LowerLeftColumn+14):
                if(j%2==0 and c<6):
                    canvas[self.UpperLeftRow+2][j]=Back.BLACK +' '
                    c=c+1
                    
            canvas[self.UpperLeftRow+2][self.LowerLeftColumn+13]=Back.BLACK+' '

            for i in range(self.LowerLeftColumn+2,self.LowerLeftColumn+9):
                canvas[self.LowerLeftRow-1][i]=Back.BLACK+' '
            for i in range(self.LowerLeftColumn+3,self.LowerLeftColumn+8):
                if(i%5==0):
                    canvas[self.LowerLeftRow-2][i]=Back.BLACK+' '
                else:
                    canvas[self.LowerLeftRow-2][i]=Back.BLACK+' '
            for i in range(self.LowerLeftRow-4,self.LowerLeftRow-2):
                for j in range(self.LowerLeftColumn+1,self.LowerLeftColumn+14):
                    if(j%3==0):
                        canvas[i][j]=Back.BLACK+' '
                    else:
                        canvas[i][j]=Back.BLACK+' '



    def CannonFire(self,barbs,archers,king):
        minBarb=barbs[0]
        mindist_barb=100000
        for barb in barbs:
            if (dis(barb.r,barb.c,self.cr,self.cc)<mindist_barb and barb.existence==1 and barb.health>0):
                mindist_barb=dis(barb.r,barb.c,self.cr,self.cc)
                minBarb=barb
        minArch=archers[0]
        mindist_arch=100000
        for arch in archers:
            if (dis(arch.r,arch.c,self.cr,self.cc)<mindist_arch and arch.existence==1 and arch.health>0):
                mindist_arch=dis(arch.r,arch.c,self.cr,self.cc)
                minArch=arch
        
        mindist_king=dis(king.r+3,king.c+1,self.cr,self.cc)
        tmparr =[mindist_arch,mindist_barb,mindist_king]
        reqArr=[]
        for x in tmparr:
            if(x <= self.range):
                reqArr.append(x)
        if(len(reqArr)>0 and min(reqArr)==mindist_arch and minArch.health>0 ):
            minArch.health = minArch.health -self.damage
        elif(len(reqArr)>0 and min(reqArr)==mindist_barb and minBarb.health>0 ):
            minBarb.health = minBarb.health -self.damage
        elif(len(reqArr)>0 and min(reqArr)==mindist_king and king.health>0 ):
            king.health = king.health -self.damage
        


class WizTower(Building):
    def __init__(self,ur,uc,lr,lc):
        Building.__init__(self,ur,uc,lr,lc)
        self.health = 350
        self.damage = 2
        self.range= 26

    def AddTower(self,canvas):
        if(self.health>0):
            self.healthPercent=(self.health/350)*100
            Building.addBuilding(self,canvas)
            for i in range(self.LowerLeftColumn+2,self.LowerLeftColumn+14):
                canvas[self.LowerLeftRow-1][i]=Back.LIGHTBLUE_EX+Fore.BLACK+'_'
            for i in range(self.LowerLeftColumn+3,self.LowerLeftColumn+13):
                canvas[self.LowerLeftRow-2][i]=Back.LIGHTBLUE_EX+Fore.BLACK+' '
                
            for i in range(self.LowerLeftColumn+5,self.LowerLeftColumn+12):
                canvas[self.LowerLeftRow-3][i]=Back.BLUE+Fore.BLACK+' '
            for i in range(self.LowerLeftColumn+6,self.LowerLeftColumn+11):
                canvas[self.LowerLeftRow-4][i]=Back.BLUE+Fore.BLACK+' '
            canvas[self.LowerLeftRow-5][self.LowerLeftColumn+8]=Back.BLUE+Fore.BLACK+' '
            canvas[self.LowerLeftRow-5][self.LowerLeftColumn+9]=Back.BLUE+Fore.WHITE+' '
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+8]=Back.BLACK+Fore.BLACK+'🧙'
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+9]=Back.BLACK+''
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+10]=Back.BLACK+Fore.BLACK+'🪄'
            
        else:
            c=0
            Building.RemoveBuilding(self,canvas)
            for i in range(self.LowerLeftColumn+2,self.LowerLeftColumn+14):
                canvas[self.LowerLeftRow-1][i]=Back.BLACK+' '
            for i in range(self.LowerLeftColumn+3,self.LowerLeftColumn+13):
                canvas[self.LowerLeftRow-2][i]=Back.BLACK+' '
                
            for i in range(self.LowerLeftColumn+5,self.LowerLeftColumn+12):
                canvas[self.LowerLeftRow-3][i]=Back.BLACK+' '
            for i in range(self.LowerLeftColumn+6,self.LowerLeftColumn+11):
                canvas[self.LowerLeftRow-4][i]=Back.BLACK+' '
            canvas[self.LowerLeftRow-5][self.LowerLeftColumn+8]=Back.BLACK+' '
            canvas[self.LowerLeftRow-5][self.LowerLeftColumn+9]=Back.BLACK+' '
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+8]=Back.BLACK+' '
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+9]=Back.BLACK+' '
            canvas[self.LowerLeftRow-6][self.LowerLeftColumn+10]=Back.BLACK+' '



    def WizFire(self,barbs,archers,balls,king):
        minBarb=barbs[0]
        mindist_barb=100000
        for barb in barbs:
            if (dis(barb.r,barb.c,self.cr,self.cc)<mindist_barb and barb.existence==1 and barb.health>0):
                mindist_barb=dis(barb.r,barb.c,self.cr,self.cc)
                minBarb=barb
        minArch=archers[0]
        mindist_arch=100000
        for arch in archers:
            if (dis(arch.r,arch.c,self.cr,self.cc)<mindist_arch and arch.existence==1 and arch.health>0):
                mindist_arch=dis(arch.r,arch.c,self.cr,self.cc)
                minArch=arch
        minball=balls[0]
        mindist_ball=100000
        for ball in balls:
            if (dis(ball.r,ball.c,self.cr,self.cc)<mindist_ball and ball.existence==1 and ball.health>0):
                mindist_ball=dis(ball.r,ball.c,self.cr,self.cc)
                minball=ball
        mindist_king=dis(king.r+3,king.c+1,self.cr,self.cc)
        tmparr =[mindist_arch,mindist_barb,mindist_ball,mindist_king]
        reqArr=[]
        for x in tmparr:
            if(x <= self.range):
                reqArr.append(x)
        if(len(reqArr)>0 and min(reqArr)==mindist_arch and minArch.health>0 ):
            minArch.health = minArch.health -self.damage
            for barb in barbs:
                if(dis(barb.r,barb.c,minArch.r,minArch.c)<5 and barb.health>0 and barb!=minBarb):
                    barb.health-=self.damage
            for arch in archers:
                if(dis(arch.r,arch.c,minArch.r,minArch.c)<5 and arch.health>0):
                    arch.health-=self.damage
            for ball in balls:
                if(dis(ball.r,ball.c,minArch.r,minArch.c)<5 and ball.health>0):
                    ball.health-=self.damage
            if(dis(king.r,king.c,minArch.r,minArch.c)<5 and king.health>0):
                king.health -= self.damage
        elif(len(reqArr)>0 and min(reqArr)==mindist_barb and minBarb.health>0 ):
            minBarb.health = minBarb.health -self.damage
            for barb in barbs:
                if(dis(barb.r,barb.c,minBarb.r,minBarb.c)<5 and barb.health>0):
                    barb.health-=self.damage
            for arch in archers:
                if(dis(arch.r,arch.c,minBarb.r,minBarb.c)<5 and arch.health>0 and arch!=minArch):
                    arch.health-=self.damage
            for ball in balls:
                if(dis(ball.r,ball.c,minBarb.r,minBarb.c)<5 and ball.health>0):
                    ball.health-=self.damage
            if(dis(king.r,king.c,minBarb.r,minBarb.c)<5 and king.health>0):
                king.health -= self.damage
        elif(len(reqArr)>0 and min(reqArr)==mindist_ball and minball.health>0 ):
            minball.health = minball.health -self.damage
            for barb in barbs:
                if(dis(barb.r,barb.c,minball.r,minball.c)<5 and barb.health>0):
                    barb.health-=self.damage
            for arch in archers:
                if(dis(arch.r,arch.c,minball.r,minball.c)<5 and arch.health>0):
                    arch.health-=self.damage
            for ball in balls:
                if(dis(ball.r,ball.c,minball.r,minball.c)<5 and ball.health>0 and ball!=minball):
                    ball.health-=self.damage
            if(dis(king.r,king.c,minball.r,minball.c)<5 and king.health>0):
                king.health -= self.damage
        elif(len(reqArr)>0 and min(reqArr)==mindist_king and king.health>0 ):
            king.health = king.health -self.damage
            for barb in barbs:
                if(dis(barb.r,barb.c,king.r,king.c)<5 and barb.health>0):
                    barb.health-=self.damage
            for arch in archers:
                if(dis(arch.r,arch.c,king.r,king.c)<5 and arch.health>0):
                    arch.health-=self.damage
            for ball in balls:
                if(dis(ball.r,ball.c,king.r,king.c)<5 and ball.health>0):
                    ball.health-=self.damage
            
        

















        