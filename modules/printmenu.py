from . import config as cfg
from .i18n import I18n
from rich.console import Console
import shutil
# 80 and less small ascii 81 ando more big ascii
console = Console()
terminal = shutil.get_terminal_size()

def printmenu(language, v, smascii):
    global i18n
    i18n = I18n(language)
    if smascii == 0 :
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
    elif smascii == 1 :
            print(f"""
   _   _    _    ___   _   _    ___ 
  /_\ | |  | |  / __| /_\ | |  / __|
 / _ \| |__| |_| (__ / _ \| |_| (__ 
/_/ \_\____|____\___/_/ \_\____\___|
V {v}
By Denis Varga made with <3 and code in Python 3.11.4

""")
    print (i18n.get("textonpick.main"))
    if cfg.load_active_option() == "1":
        console.print (f"[#1E3A8A]{i18n.get('1.main.pick')}[/#1E3A8A]")
    else:
        print (i18n.get("1.main.pick"))
    if cfg.load_active_option() == "2":
        console.print (f"[#1E3A8A]{i18n.get('2.main.pick')}[/#1E3A8A]")
    else:
        print (i18n.get("2.main.pick"))
    if cfg.load_active_option() == "3":
        console.print (f"[#1E3A8A]{i18n.get('3.main.pick')}[/#1E3A8A]")
    else:
        print (i18n.get("3.main.pick"))
    if cfg.load_active_option() == "4":
        console.print (f"[#1E3A8A]{i18n.get('4.main.pick')}[/#1E3A8A]")
    else:
        print (i18n.get("4.main.pick"))
    if cfg.load_active_option() == "5":
        console.print (f"[#1E3A8A]{i18n.get('5.main.pick')}[/#1E3A8A]")
    else:
        print (i18n.get("5.main.pick"))
    print (i18n.get("set.main.pick"))
    print (i18n.get("quit.main.pick"))
    
    