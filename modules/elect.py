from .i18n import I18n


def ohmlaw(language):
    i18n = I18n(language)
    print(f"1. {i18n.get('voltage.elect')}")
    print(f"2. {i18n.get('resistance.elect')}")
    print(f"3. {i18n.get('current.elect')}")
    unknown = input(i18n.get("pls.select.unknown.elect"))
    if unknown == "1":
        print(i18n.get("pls.provide.known.elect"))
        r = float(input(f"{i18n.get('resistance.elect')}: "))
        i = float(input(f"{i18n.get('current.elect')}: "))
        u = r * i
        print(f"{i18n.get('voltage.is.elect')}{u} V")
    elif unknown == "2":
        print(i18n.get("pls.provide.known.elect"))
        u = float(input(f"{i18n.get('voltage.elect')}: "))
        i = float(input(f"{i18n.get('current.elect')}: "))
        r = u / i
        print(f"{i18n.get('resistance.is.elect')}{r} Ω")
    elif unknown == "3":
        print(i18n.get("pls.provide.known.elect"))
        u = float(input(f"{i18n.get('voltage.elect')}: "))
        r = float(input(f"{i18n.get('resistance.elect')}: "))
        i = u / r
        print(f"{i18n.get('current.is.elect')}{i} A")


def run(language):
    i18n = I18n(language)
    print(i18n.get("welcome.elect"))
    print(i18n.get("select.calc.elect"))
    print(f"1. {i18n.get('ohms.law.elect')}")
    pick = input(i18n.get("pls.select.elect"))
    if pick == "1":
        ohmlaw(language)
