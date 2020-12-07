''' 
  Micropython mit ESP32
  Benannte Platzhalter
  
  Version 1.00, 17.10.2019
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

text = "Das Resultat von {Rechnung} ist {Resultat}"
print(text.format(Rechnung="3 x 5", Resultat = 3*5))
print(text.format(Resultat = 3*5, Rechnung="3 x 5"))

text = "Das Resultat von {Rechnung} ist {Resultat:4.2f}"
print(text.format(Resultat = 6 / 4, Rechnung="6 / 4"))

