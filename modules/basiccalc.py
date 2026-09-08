import os 
import time
from simpleeval import simple_eval
from rich.console import Console
from . import basic as bs 
from .i18n import I18n 

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    

clear_screen()
  
    
def shell(language):
    i18n = I18n(language)
    while True:
        expresion = console.input(f"[bold #2563EB]BasicCalc> [/bold #2563EB]")# prompt.shell
        if expresion.lower() == 'exit':
            print(i18n.get('exit.msg.shell'))#exit.msg.shell
            print(i18n.get('exit.msg'))#exit.msg
            exit()
        elif expresion.lower() == "help":
            print(i18n.get("help.msg.calc"))#help.msg.calc
            console.print(f"[bold #1E3A8A]{i18n.get('exit')}[/bold #1E3A8A] {i18n.get('help.msg.exit')}")
            console.print(f"[bold #1E3A8A]{i18n.get('clear')}[/bold #1E3A8A] {i18n.get('help.msg.clear')}")
            console.print(f"[bold #1E3A8A]{i18n.get('back')}[/bold #1E3A8A] {i18n.get('help.msg.back')}")
            console.print(f"[bold #1E3A8A]{i18n.get('help')}[/bold #1E3A8A] {i18n.get('help.msg.help')}")

        elif expresion.strip() == "":
            continue  # Ignore empty input
        elif expresion.lower() == "clear":
            clear_screen()
        elif expresion.lower() == "back":
            print(i18n.get("back.msg.shell"))#back.msg.shell
            bs.restart_app()
        elif expresion.lower() == "ai":
            print(i18n.get("ai.msg.shell"))#ai.msg.shell
        
        else:
            try:
                result = simple_eval(expresion)
                print(f"Result: {result}")
            except Exception as e:
                print(f"{i18n.get('error')}  {e}. {i18n.get('error.msg.shell')}.")#error, #error.msg.shell
        
def calc(language):
    i18n = I18n(language)
    clear_screen()
    print (i18n.get("welcome.msg.shell"))#welcome.msg.shell
    print (i18n.get("welcome.msg.shell2"))#welcome.msg.shell2
    shell(language)