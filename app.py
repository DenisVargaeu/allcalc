
from modules import negativecheck as ng
from modules import evenodd as eo
from modules import grade as gr
from modules import basiccalc as basic
from modules import surface as su
from rich.prompt import Prompt
import time
from modules import settings as st


print("""
   ░███    ░██         ░██           ░██████      ░██     ░██          ░██████  
  ░██░██   ░██         ░██          ░██   ░██   ░██ ░██   ░██         ░██   ░██ 
 ░██  ░██  ░██         ░██         ░██         ░██   ░██  ░██         ░██        
░█████████ ░██         ░██         ░██         ░█████████ ░██         ░██        
░██    ░██ ░██         ░██         ░██         ░██    ░██ ░██         ░██        
░██    ░██ ░██         ░██          ░██   ░██  ░██    ░██ ░██          ░██   ░██ 
░██    ░██ ░████████   ░████████     ░██████   ░██    ░██ ░████████     ░██████ 
V 2.1.1
By Denis Varga made with <3 and code in Python 3.11.4

""")
print ("Please choose what you want to calculate:")
print ("1. Check if number is positive, negative or zero")
print ("2. Check if number is even or odd")
print ("3. Check your grade")   
print ("4. Basic calcualtor shell")
print ("5. Surface calculator")
print ("SET. Settings")
print ("Q. Exit the program")

def pick(choice):

    if choice == "1":
        print ("You have chosen negative/positive chceker please provide you number")
        number = float(input("Please input a number: "))
        ng.check(number)
    elif choice == "2":
        print ("You have chosen even/odd chceker please provide you number")    
        number = float(input("Please input a number: "))
        eo.check(number)
    elif choice == "3":
        print ("You have chosen grade checker please provide you score")
        score = float(input("Please input your score: "))
        gr.check(score)
    elif choice == "4":
        print ("You have chosen basic calculator shell")
        basic.calc()
    elif choice == "5":
        print ("You have chosen Surface Calculator")
        su.run()
    elif choice == "Q" or choice == "q":
        print ("Exiting the program. Goodbye!")
        time.sleep(2)
        basic.clear_screen()
        exit()
    elif choice == "DEBUG" or choice == "debug":  # debug secret
        print("Debug mode activated.")
        su.run()
    elif choice == "SET" or choice == "set":
        st.run()
    else:
        print ("Invalid choice. Please choose 1, 2 or 3.")

while True:
    choice = Prompt.ask("[bold dark_green]Please input your choice[/bold dark_green]")
    pick(choice)
