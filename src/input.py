"""Defining input class."""
import sys
import termios
import tty
import signal
from time import sleep

class Get:
    """Class to get input."""

    def __call__(self):
        """Defining __call__."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = str(sys.stdin.read(1))
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def alarmHandler(self,signum, frame):
        """Handling timeouts."""
        raise TimeoutError

    def get_input(self, timeout=0.1):
        """Taking input from user."""
        signal.signal(signal.SIGALRM, self.alarmHandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = self.__call__()
            signal.alarm(0)
            if(text == '\x1b' or text == 'q' or text=='Q'):
                text = "q"
            elif(text == 'A' or text == 'a'):
                text = "left"
            elif(text == 'S' or text == 's'):
                text = "down"
            elif(text == 'D' or text == 'd'):
                text = "right"
            elif(text == 'W' or text == 'w'):
                text = "up"
            elif(text == 'J' or text =='j'):
                text = "King1"
            elif(text == 'I' or text =='i'):
                text = "King2"
            elif(text == 'L' or text == 'l'):
                text = "King3"
            elif(text == '1'):
                text = "Arch1"
            elif(text == '2'):
                text = "Arch2"
            elif(text == '3'):
                text = "Arch3"
            elif(text == '4'):
                text = "Barb1"
            elif(text == '5'):
                text = "Barb2"
            elif(text == '6'):
                text = "Barb3"
            elif(text == '7'):
                text = "Ball1"
            elif(text == '8'):
                text = "Ball2"
            elif(text == '9'):
                text = "Ball3"
            elif(text == ' '):
                text = "attack"
            elif(text == 'H' or text== 'h'):
                text = "Heal"
            elif(text == 'R'or text=='r'):
                text = "Rage"
            elif(text=='\n' or text=='n' or text=='N'):
                text ="Next"
            else:
                text = None
            sleep(timeout)
            return text
        except TimeoutError:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None