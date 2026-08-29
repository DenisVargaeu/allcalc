




def cube(a):
    work = a*a
    return  6* work

def cuboid(a, b, c):
    ab = (a*b)
    ac = (a*c)
    bc = (b*c)
    return 2*(ab + ac + bc) 
    
def pick(shape):
    if shape == 1:
        print ("You have selected Cube")
        a = float(input("Please enter length of side a:"))
        print(f"Surface area of cube with side length a = {a} is {cube(a)} cm²")
        return
    if shape == 2:
        print ("You have selected Cuboid")
        a = float(input("Please enter length of side a:"))
        b = float(input("Please enter length of side b:"))
        c = float(input("Please enter length of side c:"))
        print(f"Surface area of cuboid with side lengths a = {a}, b = {b}, c = {c} is {cuboid(a, b, c)} cm²")
        return

def run():
    print ("1. Cube")
    print ("2. Cuboid")
    shap = int(input("Please select a shape:"))
    pick(shap)
