# math modules
from modules import negativecheck as ng
from modules import evenodd as eo
from modules import grade as gr
from modules import basiccalc as basic
from modules import surface as su
from modules import settings as st
# config
from modules.i18n import I18n
from modules import config as cfg
from modules import printmenu as pm
# misc 
from rich.prompt import Prompt
from rich.console import Console
import time

version = "4.0.0"
lang = cfg.load_language()  
i18n = I18n(lang)
console = Console(style="white")


print(f"""
   ░███    ░██         ░██           ░██████      ░██     ░██           ░██████  
  ░██░██   ░██         ░██          ░██   ░██   ░██ ░██   ░██          ░██   ░██ 
 ░██  ░██  ░██         ░██         ░██         ░██   ░██  ░██         ░██        
░█████████ ░██         ░██         ░██         ░█████████ ░██         ░██        
░██    ░██ ░██         ░██         ░██         ░██    ░██ ░██         ░██        
░██    ░██ ░██         ░██          ░██   ░██  ░██    ░██ ░██          ░██   ░██ 
░██    ░██ ░████████   ░████████     ░██████   ░██    ░██ ░████████     ░██████ 
V {version}
By Denis Varga made with <3 and code in Python 3.11.4

""")
pm.printmenu(lang)

def pick(choice, sk):
    global lang

    if choice == "1":
        print(i18n.get("pls.provide.pos.neg.main"))

        if sk == 1:
            number = float(input(i18n.get("pls.num.inp.main")))
            cfg.save_acive_option("0")
            ng.check(number, lang)
        else:
            cfg.save_acive_option("1")
            st.restart_app()

    elif choice == "2":
        print(i18n.get("pls.provide.even.odd.main"))

        if sk == 1:
            number = float(input(i18n.get("pls.num.inp.main")))
            cfg.save_acive_option("0")
            eo.check(number, lang)
        else:
            cfg.save_acive_option("2")
            st.restart_app()

    elif choice == "3":
        print(i18n.get("pls.provide.grade.main"))

        if sk == 1:
            score = float(input(i18n.get("pls.score.inp.main")))
            cfg.save_acive_option("0")
            gr.check(score, lang)
        else:
            cfg.save_acive_option("3")
            st.restart_app()

    elif choice == "4":
        print(i18n.get("choose.basic.calc.main"))

        if sk == 1:
            cfg.save_acive_option("0")
            basic.calc(lang)
        else:
            cfg.save_acive_option("4")
            st.restart_app()

    elif choice == "5":
        print(i18n.get("choose.surface.calc.main"))

        if sk == 1:
            cfg.save_acive_option("0")
            su.run(lang)
        else:
            cfg.save_acive_option("5")
            st.restart_app()

    elif choice == "Q" or choice == "q":
        print(i18n.get("exit.msg"))
        time.sleep(2)
        basic.clear_screen()
        exit()

    elif choice == "DEBUG" or choice == "debug":
        print(i18n.get("debug.msg"))
        su.run()

    elif choice == "SET" or choice == "set":
        st.run(lang)

    elif choice == "RES" or choice == "res":
        st.restart_app()

    else:
        print(i18n.get("invalid.choice.msg"))
while True:
    if cfg.load_active_option() == "0":
        choice = Prompt.ask(f"[#1E3A8A]{i18n.get('input.choice.msg')}[/#1E3A8A]")
        pick(choice, 0)
    elif cfg.load_active_option() == "1":
        pick("1", 1)
    elif cfg.load_active_option() == "2":
        pick("2", 1)
    elif cfg.load_active_option() == "3":
        pick("3", 1)
    elif cfg.load_active_option() == "4":
        pick("4", 1)
    elif cfg.load_active_option() == "5":
        pick("5", 1)