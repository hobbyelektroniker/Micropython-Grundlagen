'''
  Objektorientiert Programmierung
  Kreis und Quadrat
    
  Version 1.00, 27.02.2021
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

from tkinter import *
from kreis_klasse import KreisV1 as Kreis 
from quadrat_klasse import QuadratV1 as Quadrat

# Bildschirm erzeugen
bildschirm = Tk()
bildschirm.title('Spielerei mit 2D - Objekten')

# Spielfeld erzeugen
spielfeld = Canvas(bildschirm, width=1000, height=800, bg="yellow")
spielfeld.pack()


# Einen Kreis und ein Quadrat zeichnen
kreis = Kreis(spielfeld, x=110, y=110, radius=100)
quadrat = Quadrat(spielfeld, x=110, y=110, laenge=80, farbe="red")

bildschirm.mainloop()