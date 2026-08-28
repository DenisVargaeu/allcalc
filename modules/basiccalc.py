import os 
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    

clear_screen()

def calc():
    clear_screen()
    print ("Welcome to BasicCalc")