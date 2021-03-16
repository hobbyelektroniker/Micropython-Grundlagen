'''
  Objektorientiert Programmierung
  Kreis und Quadrat bewegen
    
  Version 1.20, 15.03.2021
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

from tkinter import *
from kreis_klasse import KreisV2 as Kreis 
from quadrat_klasse import QuadratV2 as Quadrat
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
time.sleep(5)

# Kreis und Quadrat 5000 Schritte in 3-er Schritten bewegen
kreis.bewegung(x=3, y=3)
quadrat.bewegung(x=-4, y=5)
for i in range(5000):
    kreis.bewege()
    quadrat.bewege()
    
bildschirm.mainloop()

