'''
  Objektorientiert Programmierung
  Ein bewegtes Objekt
    
  Version 1.00, 27.02.2021
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

from tkinter import *
from kreis_klasse import KreisV1 as Kreis 
from quadrat_klasse import QuadratV1 as Quadrat
from bewegt_klasse import BewegtesObjektV1 as BewegtesObjekt
import time

# Bildschirm erzeugen
bildschirm = Tk()
bildschirm.title('Spielerei mit 2D - Objekten')

# Spielfeld erzeugen
spielfeld = Canvas(bildschirm, width=1000, height=800, bg="yellow")
spielfeld.pack()


# Einen Kreis und ein Quadrat zeichnen
kreis = Kreis(spielfeld, x=110, y=110, radius=100)
quadrat = Quadrat(spielfeld, x=110, y=110, laenge=80, farbe="red")

# Ein bewegtes Objekt erstellen und für 5 Sekunden anzeigen
bewegt = BewegtesObjekt(spielfeld, x=110, y=110)
time.sleep(5)

# Die Figur 500 Schritte in 3-er Schritten bewegen
bewegt.bewegung(x=3, y=3)
for i in range(500):
    bewegt.bewege()
    
bildschirm.mainloop()

