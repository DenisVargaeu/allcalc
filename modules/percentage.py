def upp(w, p):
    o = (w/100)
    s = (o*p)
    print (f"Percentage is {s}%")
    input ("Press enter to continues")
    return
    
def pick(p):
    if p == 1:
        print ("picked 1")
        wh = (int(input ("Please enter whole (100%): ")))
        pr = (int(input ("Please enter percentage (No % symbol): ")))
        upp(wh, pr)
    else :
        print("Wrong operation")

def run():
    print ("Perctentege ")
    print ("1. Unknown percentge part")
    pc = int(input("Please select operation: "))
    pick(pc)
