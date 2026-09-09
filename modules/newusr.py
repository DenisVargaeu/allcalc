from . import settings as st
from .i18n import I18n as I18n
from . import basic as bs 
from . import config as con

def nw(langg, v):
    i18n = I18n(langg)
    print(f"""
   ░███    ░██         ░██           ░██████      ░██     ░██           ░██████  
  ░██░██   ░██         ░██          ░██   ░██   ░██ ░██   ░██          ░██   ░██ 
 ░██  ░██  ░██         ░██         ░██         ░██   ░██  ░██         ░██        
░█████████ ░██         ░██         ░██         ░█████████ ░██         ░██        
░██    ░██ ░██         ░██         ░██         ░██    ░██ ░██         ░██        
░██    ░██ ░██         ░██          ░██   ░██  ░██    ░██ ░██          ░██   ░██ 
░██    ░██ ░████████   ░████████     ░██████   ░██    ░██ ░████████     ░██████ 
V {v}
By Denis Varga made with <3 and code in Python 3.11.4

""")
    print(i18n.get("welcome.new"))
    print (i18n.get("new.msg.1"))
    input (i18n.get("press.setup.new"))
    def finish():
        print (i18n.get("gtg.new"))
        input (i18n.get("press.start.new"))
        con.edit_new("0")
        bs.restart_app()
    def pick(choice,):
        if choice == "1":
            print(i18n.get("ave.lang.settings"), i18n.getalllang())#ave.lang.settings
            lang = input(i18n.get("enter.lang.settings"))#enter.lang.settings
            con.edit_language(lang)
            bs.clear_screen()
            finish()
    def prompt():
        pick (input(i18n.get("enter.choice.settings")),)#enter.choice.settings       

    def run():
        print(i18n.get("pls.pick.settings.main"))#pls.pick.settings.main
        print("1. " + i18n.get("language.settings"))#language.settings
        prompt()
    run()
