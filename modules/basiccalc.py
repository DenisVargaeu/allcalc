import os 
import time
from simpleeval import simple_eval

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    

clear_screen()
  
    
def shell():
    while True:
        expresion = input("BasicCalc> ")
        if expresion.lower() == "exit":
            print("Exiting BasicCalc shell.")
            print("Good bye! Have a nice day!")
            exit()
        elif expresion.lower() == "help":
            print("BasicCalc shell allows you to perform basic calculations.")
            print("You can enter mathematical expressions using operators like +, -, *, /, and parentheses.")
            print("For example: 2 + 3 * (4 - 1)")
            print("Type 'exit' to exit the shell.")
        
        else:
            try:
                result = simple_eval(expresion)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}. Please enter a valid mathematical expression.")
        
def calc():
    clear_screen()
    print ("Welcome to BasicCalc shell")
    print ("For help type help and for exit type exit")
    shell()