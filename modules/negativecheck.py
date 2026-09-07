from .i18n import I18n

def check (number, language):
    i18n = I18n(language)
    if number > 0:
        print (f"{i18n.get('number')} {number} {i18n.get('positive.negposcheck')}")#Number= number 
        return
    elif number < 0:
        print (f"{i18n.get('number')} {number} {i18n.get('negative.negposcheck')}   ")
        return
    elif number == 0:
        print (f"{i18n.get('number')} {number} {i18n.get('zero.negposcheck')}")
        return