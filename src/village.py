import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
class Village:
    def __init__(self):
        self.HEIGHT = 48
        self.WIDTH = 200
        self.LEFT_PADDING=20
        self.health = 100
        self.loot = 10000

    def buildCanvasFrame(self, CANVAS):
        CANVAS[0][0] = Back.LIGHTWHITE_EX+Fore.BLUE+"╔"
        CANVAS[0][self.WIDTH - 1] = Back.LIGHTWHITE_EX+Fore.BLUE+"╗"
        CANVAS[self.HEIGHT - 1][0] = Back.LIGHTWHITE_EX+Fore.BLUE+"╚"
        CANVAS[self.HEIGHT - 1][self.WIDTH - 1] = Back.LIGHTWHITE_EX+Fore.BLUE+"╝"
        for x in range(1,self.WIDTH-1,2):
            CANVAS[0][x]=Back.LIGHTWHITE_EX+Fore.GREEN+"♧"
            CANVAS[self.HEIGHT - 1][x]=Back.LIGHTWHITE_EX+Fore.GREEN+"♧"
            if(x+1!=self.WIDTH-1):
                CANVAS[0][x+1]=Back.LIGHTWHITE_EX+Fore.GREEN+" "
                CANVAS[self.HEIGHT - 1][x+1]=Back.LIGHTWHITE_EX+Fore.GREEN+" "
        for y in range(1,self.HEIGHT-1):
            CANVAS[y][0]=Back.LIGHTWHITE_EX+Fore.GREEN+"♧"
            CANVAS[y][self.WIDTH-1]=Back.LIGHTWHITE_EX+Fore.GREEN+"♧"
            if(y+1!=self.HEIGHT-1):
                CANVAS[y+1][0]=Back.LIGHTWHITE_EX+Fore.GREEN+" "
                CANVAS[y+1][self.WIDTH-1]=Back.LIGHTWHITE_EX+Fore.GREEN+" "

    def addSpawnPoints(self,CANVAS):
        Position1r = 24
        Position1c = 15
        Position2r = 34
        Position2c = 185
        Position3r = 14
        Position3c = 185
        CANVAS[Position1r+1][Position1c+1]=Fore.GREEN+'1'
        CANVAS[Position1r+1][Position1c+2]=Fore.GREEN+' '
        CANVAS[Position1r+1][Position1c]=Fore.GREEN+' '
        CANVAS[Position2r+1][Position2c+1]=Fore.GREEN+'2'
        CANVAS[Position2r+1][Position2c+2]=Fore.GREEN+' '
        CANVAS[Position2r+1][Position2c]=Fore.GREEN+' '
        CANVAS[Position3r+1][Position3c+1]=Fore.GREEN+'3'
        CANVAS[Position3r+1][Position3c+2]=Fore.GREEN+' '
        CANVAS[Position3r+1][Position3c]=Fore.GREEN+' '