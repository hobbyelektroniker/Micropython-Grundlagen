
def ausgabe1():
    print("*** Ausgabe 1 ***")
    print(a,b,c)
    print()

def ausgabe2(a,b):
    print("*** Ausgabe 2 ***")
    # global a,b # nicht erlaubt!
    a = "Eine andere Zahl:"
    b = 7
    #global c
    #c[1] = 10
    c = [2,7,4,6,5]
    print(a,b,c)
    print()


a = "Die Zahl lautet"
b = 5
c = [1,3,5]

print("Globale Werte: a = {}, b = {}, c = {}".format(a,b,c))
ausgabe1()
print("Globale Werte: a = {}, b = {}, c = {}".format(a,b,c))
ausgabe2(a,b)
print("Globale Werte: a = {}, b = {}, c = {}".format(a,b,c))


