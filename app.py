
from modules import negativecheck as ng
from modules import evenodd as eo
from modules import grade as gr
from modules import basiccalc as basic
from modules import surface as su
from rich.prompt import Prompt
import time
from modules import settings as st
from modules.i18n import I18n

i18n = I18n("sk")


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
print (i18n.get("textonpick.main"))
print (i18n.get("1.main.pick"))
print (i18n.get("2.main.pick"))
print (i18n.get("3.main.pick"))
print (i18n.get("4.main.pick"))
print (i18n.get("5.main.pick"))
print (i18n.get("set.main.pick"))
print (i18n.get("quit.main.pick"))


def pick(choice):

    if choice == "1":
        print (i18n.get("pls.provide.pos.neg.main"))
        number = float(input(i18n.get("pls.num.inp.main")))
        ng.check(number)
    elif choice == "2":
        print (i18n.get("pls.provide.even.odd.main"))
        number = float(input(i18n.get("pls.num.inp.main")))
        eo.check(number)
    elif choice == "3":
        print (i18n.get("pls.provide.grade.main"))
        score = float(input(i18n.get("pls.score.inp.main")))
        gr.check(score)
    elif choice == "4":
        print (i18n.get("choose.basic.calc.main"))
        basic.calc()
    elif choice == "5":
        print (i18n.get("choose.surface.calc.main"))
        su.run()
    elif choice == "Q" or choice == "q":
        print (i18n.get("exit.msg"))
        time.sleep(2)
        basic.clear_screen()
        exit()
    elif choice == "DEBUG" or choice == "debug":
        print(i18n.get("debug.msg"))
        su.run()
    elif choice == "SET" or choice == "set":
        st.run()
    else:
        print(i18n.get("invalid.choice.msg"))

while True:
    choice = Prompt.ask(f"[bold dark_green]{i18n.get('input.choice.msg')}[/bold dark_green]")
    pick(choice)
