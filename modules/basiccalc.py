import os 
import time
from simpleeval import simple_eval
from rich.console import Console


console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    

clear_screen()
  
    
def shell():
    while True:
        expresion = console.input("[bold #2563EB]BasicCalc> [/bold #2563EB]")
        if expresion.lower() == "exit":
            print("Exiting BasicCalc shell.")
            print("Good bye! Have a nice day!")
            exit()
        elif expresion.lower() == "help":
            print("BasicCalc shell allows you to perform basic calculations.")
            print("You can enter mathematical expressions using operators like +, -, *, /, and parentheses.")
            console.print("[bold #1E3A8A]Type 'exit'[/bold #1E3A8A] to exit the shell.")
            console.print("[bold #1E3A8A]Type 'clear'[/bold #1E3A8A] to clear the screen.")
            console.print("[bold #1E3A8A]Type 'back'[/bold #1E3A8A] to return to the main menu.")
            console.print("[bold #1E3A8A]Type 'help'[/bold #1E3A8A] to see this message again.")
        elif expresion.strip() == "":
            continue  # Ignore empty input
        elif expresion.lower() == "clear":
            clear_screen()
        elif expresion.lower() == "back":
            print("Returning to main menu.")
            return
        elif expresion.lower() == "ai":
            print ("No ai used in this project and none will be :)")
        
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