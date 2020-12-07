''' 
  Micropython mit ESP32
  Ganze Zahlen
  
  Version 1.00, 17.10.2019
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

zahlen = [2,235,15,8,-12]

for zahl in zahlen:
    print(zahl)
print()

ausgabe = "Die Zahl ist {}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()
    
# Feste Stellenanzahl    
ausgabe = "Die Zahl ist {:4d}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Vorzeichen immer ausgeben
ausgabe = "Die Zahl ist {:+4d}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Vornullen ausgeben
ausgabe = "Die Zahl ist {:+04d}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Linksbündig
ausgabe = "Die Zahl ist {:<4d}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Rechtsbündig
ausgabe = "Die Zahl ist {:>4d}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Zentriert
ausgabe = "Die Zahl ist {:^4d}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Vorzeichen untereinander
ausgabe = "Die Zahl ist {: =+4d}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Vorzeichen untereinander, mit Vornullen
ausgabe = "Die Zahl ist {:0=+4d}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()








          
          






