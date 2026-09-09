import os
import sys

def test(number):
    print(number)
def restart_app():
    os.execl(sys.executable, sys.executable, *sys.argv)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    
