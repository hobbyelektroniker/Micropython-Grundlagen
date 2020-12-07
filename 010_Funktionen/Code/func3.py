import math

def flaeche(r=None,d=None):
    if r:
#    if r and not d:
        return r**2 * math.pi
    elif d:
#    elif d and not r:
        return d**2 * math.pi / 4
    else:
        return None
        

print(flaeche(3))
print(flaeche(r=3))
print(flaeche(d=3))
print(flaeche(3,4))


