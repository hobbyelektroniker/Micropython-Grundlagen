a = "Die Zahl lautet"
b = 5

def ausgabe1():
    print("*** Ausgabe 1 ***")
    print(a,b)
    print()

def ausgabe2():
    print("*** Ausgabe 2 ***")
    a = "Eine andere Zahl:"
    b = 7
    print(a,b)
    print()

print("Globale Werte: a = {}, b = {}".format(a,b))
ausgabe1()
print("Globale Werte: a = {}, b = {}".format(a,b))
ausgabe2()
print("Globale Werte: a = {}, b = {}".format(a,b))

