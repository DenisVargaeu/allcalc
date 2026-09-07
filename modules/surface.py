import math
from .i18n import I18n



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


def pick(shape, unit, language):
    i18n = I18n(language)
    if shape == 1:
        print (f"{i18n.get('y.have.select')}{i18n.get('cube').lower()}")# y.have.select
        a = float(input(f"{i18n.get('pls.enter.length')}a:"))
        print(f"{i18n.get('ans.cube.surface')}a = {a} {unit} {i18n.get('is')} {cube(a)} {unit}²")
        return
    elif shape == 2:
        print (f"{i18n.get('y.have.select')}{i18n.get('cuboid').lower()}")# y.have.select
        a = float(input(f"{i18n.get('pls.enter.length')}a:"))
        b = float(input(f"{i18n.get('pls.enter.length')}b:"))
        c = float(input(f"{i18n.get('pls.enter.length')}c:"))
        print(f"{i18n.get('ans.cuboid.surface')}a = {a} {unit}, b = {b} {unit}, c = {c} {unit} {i18n.get('is')} {cuboid(a, b, c)} {unit}²")
        return
    elif shape == 3:
        r = (float(input(f"{i18n.get('pls.enter.radius')}{i18n.get('sphere').lower()}: ")))
        print (f"{i18n.get('ans.sphere.surface')} = {r} {unit} {i18n.get('is')} {sphere(r)} {unit}²")

    elif shape == 4:
        r = (float(input(f"{i18n.get('pls.enter.radius')}{i18n.get('cylinder').lower()}: ")))
        h = (float(input(f"{i18n.get('pls.enter.height')}{i18n.get('cylinder').lower()}: ")))
        print (f"{i18n.get('ans.cylinder.surface')} = {r} {unit} {i18n.get('a.height')} = {h} {unit} {i18n.get('is')} {cylinder(r, h)} {unit}²")
        


def run(language):
    i18n = I18n(language)
    print (f"1. {i18n.get('cube')}")
    print (f"2. {i18n.get('cuboid')}")
    print (f"3. {i18n.get('sphere')}")
    print (f"4. {i18n.get('cylinder')}")
    shap = int(input(f"{i18n.get('pls.select.shape')}"))
    uni = input(f"{i18n.get('pls.enter.unit')}")
    pick(shap, uni, language)
