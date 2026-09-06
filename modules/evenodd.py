from .i18n import I18n
"""
This script check if inputed number is even or odd 
"""

def check(number, language):

    i18n = I18n(language)
    work = (number/2)

    if number.is_integer() and work.is_integer():
        print (f"{i18n.get('number')} {number} {i18n.get('is.even')}")
        return
    else:
        print (f"{i18n.get('number')} {number} {i18n.get('is.odd')}")
        return