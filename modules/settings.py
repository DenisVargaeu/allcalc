import json
import os
import sys
from .i18n import I18n
from . import config as con

def restart_app():
    os.execl(sys.executable, sys.executable, *sys.argv)
def pick(choice, lang):
    i18n = I18n(lang)
    if choice == "1":
        print(i18n.get("ave.lang.settings"), i18n.getalllang())#ave.lang.settings
        lang = input(i18n.get("enter.lang.settings"))#enter.lang.settings
        con.edit_language(lang)
        restart_app()
def prompt(lang):
    i18n = I18n(lang)
    pick (input(i18n.get("enter.choice.settings")), lang)#enter.choice.settings       

def run(langg):
    i18n = I18n(langg)
    print(i18n.get("pls.pick.settings.main"))#pls.pick.settings.main
    print("1. " + i18n.get("language.settings"))#language.settings
    prompt(langg)


