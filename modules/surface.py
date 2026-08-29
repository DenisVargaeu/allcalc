import math




def cube(a):
    work = a*a
    return  6* work

def cuboid(a, b, c):
    ab = (a*b)
    ac = (a*c)
    bc = (b*c)
    return 2*(ab + ac + bc) 
    
def  sphere(radius):
        
        surface = 4 * math.pi * radius ** 2
        return surface 

def cylinder(radius, height):
    surface = 2 * math.pi * radius ** 2+2 * math.pi * radius * height
    return surface


def pick(shape, unit):
    if shape == 1:
        print ("You have selected Cube")
        a = float(input("Please enter length of side a:"))
        print(f"Surface area of cube with side length a = {a} {unit} is {cube(a)} {unit}²")
        return
    elif shape == 2:
        print ("You have selected Cuboid")
        a = float(input("Please enter length of side a:"))
        b = float(input("Please enter length of side b:"))
        c = float(input("Please enter length of side c:"))
        print(f"Surface area of cuboid with side lengths a = {a} {unit}, b = {b} {unit}, c = {c} {unit} is {cuboid(a, b, c)} {unit}²")
        return
    elif shape == 3:
        r = (float(input("Please enter radius of sphere: ")))
        print (f"Surface area of sphere with radius {r} is {sphere(r)} {unit}²")

    elif shape == 4:
        r = (float(input("Please enter radius: ")))
        h = (float(input("Please enter height: ")))
        print (f"Surface area of cylinder with radius {r} {unit} and height {h} {unit} is {cylinder(r, h)} {unit}²")
        


def run():
    print ("1. Cube")
    print ("2. Cuboid")
    print ("3. Sphere")
    print ("4. Cylinder")
    shap = int(input("Please select a shape:"))
    uni = input("Please enter the unit (cm/mm/m): ")
    pick(shap, uni)
