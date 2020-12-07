

def ausgabe3(a,b,c):
    print("*** Ausgabe 3 ***")
    a = "Eine andere Zahl:"
    b = 7
    c[1] = 2
    c = [1,7,4,6,5]
    c[2] = 12
    print(a,b,c)
    print()

a = "Die Zahl lautet"
b = 5
c = [1,3,5]

print("Globale Werte: a = {}, b = {}, c = {}".format(a,b,c))
ausgabe3(a,b,c)
print("Globale Werte: a = {}, b = {}, c = {}".format(a,b,c))

