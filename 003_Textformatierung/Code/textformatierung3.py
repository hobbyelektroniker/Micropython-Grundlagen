''' 
  Micropython mit ESP32
  Floats
  
  Version 1.00, 17.10.2019
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

zahlen = [2.5,235.25,15.3,8.735,-12.37]

for zahl in zahlen:
    print(zahl)
print()

ausgabe = "Die Zahl ist {}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()
    
# Feste Stellenanzahl    
ausgabe = "Die Zahl ist {:8.4f}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Nicht zu viele Stellen ausgeben!!!    
ausgabe = "Die Zahl ist {:12.8f}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()


# Vorzeichen immer ausgeben
ausgabe = "Die Zahl ist {:+8.4f}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Vornullen ausgeben
ausgabe = "Die Zahl ist {:+08.4f}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Linksbündig
ausgabe = "Die Zahl ist {:<8.4f}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Rechtsbündig
ausgabe = "Die Zahl ist {:>8.4f}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Zentriert
ausgabe = "Die Zahl ist {:^8.4f}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Vorzeichen untereinander
ausgabe = "Die Zahl ist {: =+8.4f}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()

# Vorzeichen untereinander, mit Vornullen
ausgabe = "Die Zahl ist {:0=+8.4f}, was kommt danach?"
for zahl in zahlen:
    print(ausgabe.format(zahl))
print()








          
          






