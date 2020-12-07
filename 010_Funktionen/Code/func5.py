import math

def flaeche(**kwargs):
    print()
    print(kwargs)
    if "r" in kwargs:
        return kwargs["r"]**2 * math.pi
    elif "d" in kwargs:
        return kwargs["d"]**2 * math.pi / 4
    elif "g" in kwargs and "h" in kwargs:
        return kwargs["g"] * kwargs["h"] / 2
    elif "a" in kwargs:
        a = kwargs["a"]
        if "b" in kwargs:
            b = kwargs["b"]
        else:
            b = a
        return a * b
    else:
        return None


# print(flaeche(5)) # Kreis mit Radius r geht nicht!
print(flaeche(d=2)) # Kreis mit Durchmesser d
print(flaeche(r=2)) # Kreis mit Radius r

print(flaeche(g=5,h=2)) # Dreieck mit Grundlinie c und Höhe h
print(flaeche(a=5))     # Quadrat mit Seitenlänge a
print(flaeche(a=5,b=2)) # Rechteck mit Seiten a und b

