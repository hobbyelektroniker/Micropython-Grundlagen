print("Bitoperatoren")
a = 6
b = 7
print("a     = {:04b}".format(a))
print("b     = {:04b}".format(b))
print()

print("a & b = {:04b}".format(a & b)) # AND
print("a | b = {:04b}".format(a | b)) # OR
print("a ^ b = {:04b}".format(a ^ b)) # XOR
print()

# NOT
print("~a = {:04b} (Ausgabe mit Vorzeichen!)".format(~a)) # gibt Probleme bei der Ausgabe
print()

# SHIFT
print("001101000 >> 2 = {:09b}".format(0b001101000 >> 2)) # um 2 Positionen nach rechts verschieben
print("001101000 << 2 = {:09b}".format(0b001101000 << 2)) # um 2 Positionen nach links verschieben

