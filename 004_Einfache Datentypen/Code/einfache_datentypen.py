''' 
  Micropython Grundlagen
  Einfache Datentypen
  
  Version 1.00, 15.12.2019
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

ganze_zahl = 10
dezimalzahl = 5.75
zeichen = 'A'
komplexe_zahl = 3.5 + 2.5j
text = "2.5"
ja_nein = True

print("Alle Variablen ausgeben")
print(ganze_zahl)
print(dezimalzahl)
print(zeichen)
print(komplexe_zahl)
print(text)
print(ja_nein)
print("------------------------")
print()


print("Als int ausgeben")
print(int(ganze_zahl))
print(int(dezimalzahl))
print("int(zeichen) geht nicht, verwende ord(zeichen)")
print(ord(zeichen))
print("int(komplexe_zahl) geht nicht")
print("int(text) geht nicht")
print(int(ja_nein))
print("------------------------")
print()

print("Als float ausgeben")
print(float(ganze_zahl))
print(float(dezimalzahl))
print("float(zeichen) geht nicht")
print("float(komplexe_zahl) geht nicht")
print(float(text))
print(float(ja_nein))
print("------------------------")
print()

print("Als complex ausgeben")
print(complex(ganze_zahl))
print(complex(dezimalzahl))
print("complex(zeichen) geht nicht")
print(complex(komplexe_zahl))
print(complex(text))
print(complex(ja_nein))
print("------------------------")
print()

print("Als str ausgeben")
print(str(ganze_zahl))
print(str(dezimalzahl))
print(str(zeichen))
print(str(komplexe_zahl))
print(str(text))
print(str(ja_nein))
print("------------------------")
print()

print("Als bool ausgeben")
print(bool(ganze_zahl))
print(bool(dezimalzahl))
print(bool(zeichen))
print(bool(komplexe_zahl))
print(bool(text))
print(bool(ja_nein))
print("------------------------")
print()








