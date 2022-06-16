import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Wall:
    def __init__(self,r,c):
        self.health = 75
        self.healthPercent = 100
        self.row =r
        self.column = c
    
    def AddWall(self,canvas):
        if(self.health>0):
            canvas[self.row][self.column] = Fore.LIGHTWHITE_EX+Back.BLUE+'⚵'
        else:
            self.RemoveWall(canvas)
    def RemoveWall(self,canvas):
        self.health=0
        self.healthPercent=0
        canvas[self.row][self.column] = Back.BLACK +' '
        self.row=0
        self.column=0
        

