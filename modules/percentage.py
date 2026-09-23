def upp(w, p):
    o = (w/100)
    s = (o*p)
    print (f"Percentage is {s}%")
    input ("Press enter to continues")
    return
def up(pp, w):
    w1 = (w/100)
    a = (pp/w1)
    print (f"Percentage is {a}%")
    input ("Press enter to continues")
    return
def pick(p):
    if p == 1:
        print ("picked 1")
        wh = (int(input ("Please enter whole (100%): ")))
        pr = (int(input ("Please enter percentage (No % symbol): ")))
        upp(wh, pr)
    if p == 2:
        print ("picked 2")
        ww = (int(input ("Please enter whole (100%): ")))
        pr = (int(input ("Please enter percentage part: ")))
        up(pr, ww)
    else :
        print("Wrong operation")

def run():
    print ("Perctentege ")
    print ("1. Unknown percentge part")
    print ("2. Unknown percentage")

    pc = int(input("Please select operation: "))
    pick(pc)
