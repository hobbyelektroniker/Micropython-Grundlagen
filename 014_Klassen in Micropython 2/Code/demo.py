'''
  Objektorientiert Programmierung
  Eine Demo mit mehreren Objekten
    
  Version 1.0, 15.03.2021
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

from tkinter import *
from kreis_klasse import KreisV2 as Kreis 
from quadrat_klasse import QuadratV2 as Quadrat

# Bildschirm erzeugen
bildschirm = Tk()
bildschirm.title('Spielerei mit 2D - Objekten')

# Spielfeld erzeugen
spielfeld = Canvas(bildschirm, width=1000, height=800, bg="yellow")
spielfeld.pack()

# Objekte erzeugen
kreis1 = Kreis(spielfeld, x=110, y=110, radius=100)
quadrat1 = Quadrat(spielfeld, x=110, y=110, laenge=80, farbe="red")
kreis2 = Kreis(spielfeld, x=210, y=210, radius=50, farbe="blue")
quadrat2 = Quadrat(spielfeld, x=300, y=350, laenge=120, farbe="green")

# Objekte bewegen
kreis1.bewegung(x=6, y=6)
quadrat1.bewegung(x=-8, y=10)
kreis2.bewegung(x=10, y=-4)
quadrat2.bewegung(x=-4, y=-6)
while(True):
    kreis1.bewege()
    quadrat1.bewege()
    kreis2.bewege()
    quadrat2.bewege()
    