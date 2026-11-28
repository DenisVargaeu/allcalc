from .i18n import I18n


def ecc(language):
    i18n = I18n(language)
    print(f"1. {i18n.get('charge.elect')}")
    print(f"2. {i18n.get('current.elect')}")
    print(f"3. {i18n.get('time.elect')}")
    pick = input(i18n.get("pls.select.unknown.elect"))
    if pick == "1":
        print(i18n.get("pls.provide.known.elect"))
        i = float(input(f"{i18n.get('current.elect')}: "))
        t = float(input(f"{i18n.get('time.elect')}: "))
        q = i * t
        print(f"{i18n.get('charge.is.elect')}{q} C")
    elif pick == "2":
        print(i18n.get("pls.provide.known.elect"))
        q = float(input(f"{i18n.get('charge.elect')}: "))
        t = float(input(f"{i18n.get('time.elect')}: "))
        i = q / t
        print(f"{i18n.get('current.is.elect')}{i} A")
    elif pick == "3":
        print(i18n.get("pls.provide.known.elect"))
        q = float(input(f"{i18n.get('charge.elect')}: "))
        i = float(input(f"{i18n.get('current.elect')}: "))
        t = q / i
        print(f"{i18n.get('time.is.elect')}{t} s")


def elpow(language):
    i18n = I18n(language)

    print(f"1. {i18n.get('current.elect')}")
    print(f"2. {i18n.get('voltage.elect')}")
    print(f"3. {i18n.get('power.elect')}")
    pick = input(i18n.get("pls.select.unknown.elect"))
    if pick == "1":
        print(i18n.get("pls.provide.known.elect"))
        u = float(input(f"{i18n.get('voltage.elect')}: "))
        p = float(input(f"{i18n.get('power.elect')}: "))
        i = p / u
        print(f"{i18n.get('current.is.elect')}{i} A")
    elif pick == "2":
        print(i18n.get("pls.provide.known.elect"))
        i = float(input(f"{i18n.get('current.elect')}: "))
        p = float(input(f"{i18n.get('power.elect')}: "))
        u = p / i
        print(f"{i18n.get('voltage.is.elect')}{u} V")
    elif pick == "3":
        print(i18n.get("pls.provide.known.elect"))
        i = float(input(f"{i18n.get('current.elect')}: "))
        u = float(input(f"{i18n.get('voltage.elect')}: "))
        p = i * u
        print(f"{i18n.get('power.is.elect')}{p} W")


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
    print(f"2. {i18n.get('el.power.elect')}")
    print(f"3. {i18n.get('el.charge.elect')}")
    pick = input(i18n.get("pls.select.elect"))
    if pick == "1":
        ohmlaw(language)
    elif pick == "2":
        elpow(language)
    elif pick == "3":
        ecc(language)
