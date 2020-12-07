a = "Die Zahl lautet"
b = 5

def ausgabe1():
    print("*** Ausgabe 1 ***")
    print(a,b)
    print()

def ausgabe2():
    print("*** Ausgabe 2 ***")
    global a,b,c
    a = "Eine andere Zahl:"
    b = 7
    c = 10
    print(a,b)
    print()

print("Globale Werte: a = {}, b = {}".format(a,b))
ausgabe1()
print("Globale Werte: a = {}, b = {}".format(a,b))
ausgabe2()
print("Globale Werte: a = {}, b = {}".format(a,b))
print(c)
