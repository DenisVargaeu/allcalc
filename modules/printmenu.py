from . import config as cfg
from .i18n import I18n
from rich.console import Console

console = Console()

def printmenu(language):
    global i18n
    i18n = I18n(language)
    if cfg.load_active_option() == "1":
        print (i18n.get("textonpick.main"))
        console.print (f"[#1E3A8A]{i18n.get('1.main.pick')}[/#1E3A8A]")
        print (i18n.get("2.main.pick"))
        print (i18n.get("3.main.pick"))
        print (i18n.get("4.main.pick"))
        print (i18n.get("5.main.pick"))
        print (i18n.get("set.main.pick"))
        print (i18n.get("quit.main.pick"))
    if cfg.load_active_option() == "2":
        print (i18n.get("textonpick.main"))
        print (i18n.get("1.main.pick"))
        console.print (f"[#1E3A8A]{i18n.get('2.main.pick')}[/#1E3A8A]")
        print (i18n.get("3.main.pick"))
        print (i18n.get("4.main.pick"))
        print (i18n.get("5.main.pick"))
        print (i18n.get("set.main.pick"))
        print (i18n.get("quit.main.pick"))
    if cfg.load_active_option() == "3":
        print (i18n.get("textonpick.main"))
        print (i18n.get("1.main.pick"))
        print (i18n.get("2.main.pick"))
        console.print (f"[#1E3A8A]{i18n.get('3.main.pick')}[/#1E3A8A]")
        print (i18n.get("4.main.pick"))
        print (i18n.get("5.main.pick"))
        print (i18n.get("set.main.pick"))
        print (i18n.get("quit.main.pick"))
    if cfg.load_active_option() == "4":
        print (i18n.get("textonpick.main"))
        print (i18n.get("1.main.pick"))
        print (i18n.get("2.main.pick"))
        print (i18n.get("3.main.pick"))
        console.print (f"[#1E3A8A]{i18n.get('4.main.pick')}[/#1E3A8A]")
        print (i18n.get("5.main.pick"))
        print (i18n.get("set.main.pick"))
        print (i18n.get("quit.main.pick"))
    if cfg.load_active_option() == "5":
        print (i18n.get("textonpick.main"))
        print (i18n.get("1.main.pick"))
        print (i18n.get("2.main.pick"))
        print (i18n.get("3.main.pick"))
        print (i18n.get("4.main.pick"))
        console.print (f"[#1E3A8A]{i18n.get('5.main.pick')}[/#1E3A8A]")
        print (i18n.get("set.main.pick"))
        print (i18n.get("quit.main.pick"))
    if cfg.load_active_option() == "0":
        print (i18n.get("textonpick.main"))
        print (i18n.get("1.main.pick"))
        print (i18n.get("2.main.pick"))
        print (i18n.get("3.main.pick"))
        print (i18n.get("4.main.pick"))
        print (i18n.get("5.main.pick"))
        print (i18n.get("set.main.pick"))
        print (i18n.get("quit.main.pick"))
    