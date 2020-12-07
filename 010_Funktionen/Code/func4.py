import math

def flaeche(r=None,d=None,g=None,h=None,a=None,b=None):
    if r:
        return r**2 * math.pi
    elif d:
        return d**2 * math.pi / 4
    elif g and h:
        return g * h / 2
    elif a:
        if not b: b = a
        return a * b
    else:
        return None
        

print(flaeche(5))   # Kreis mit Radius r
print(flaeche(d=2)) # Kreis mit Durchmesser d
print(flaeche(r=2)) # Kreis mit Radius r

print(flaeche(g=5,h=2)) # Dreieck mit Grundlinie g und Höhe h
print(flaeche(a=5))     # Quadrat mit Seitenlänge a
print(flaeche(a=5,b=2)) # Rechteck mit Seiten a und b


