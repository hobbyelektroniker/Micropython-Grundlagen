''' 
  Micropython mit ESP32
  Textformatierung Grundlagen
  
  Version 1.00, 17.10.2019
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

print("Das ist ein String")

rechnung = "3 * 5"
print("Das Resultat von {} ist {}".format(rechnung,3*5))

rechnung = "13 / 5"
print("Das Resultat von {} ist {}".format(rechnung,eval(rechnung)))

print()

print("In der Sprache C werden Blöcke in {} eingeschlossen.")
#print("In der Sprache {} werden Blöcke in {} eingeschlossen.".format("C"))
print("In der Sprache {} werden Blöcke in {{}} eingeschlossen.".format("C"))

text = "In der Sprache {} werden Blöcke in {} eingeschlossen."
print(text.format("C","{}"))
print(text.format("Pascal","begin end"))

text = "Für {:10} brauchen wir viel Platz."
print(text.format("HALLO"))

# linksbündig
text = "Für {:<10} brauchen wir viel Platz."
print(text.format("HALLO"))

# rechtsbündig
text = "Für {:>10} brauchen wir viel Platz."
print(text.format("HALLO"))

# eingemittet
text = "Für {:^10} brauchen wir viel Platz."
print(text.format("HALLO"))