'''
  Objektorientiert Programmierung
  Eine Klasse für ein Quadrat
    
  Version 1.10, 15.03.2021
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

# Quadrat
import math
from bewegt_klasse import BewegtesObjektV3 as BewegtesObjekt

# Diese Klasse zeichnet ein Quadrat, das auf einer Ecke steht
# fenster: das Fenster, in dem der Kreis gezeichnet werden soll
# x, y: x und y Koordinaten des Mittelpunkts
# laenge: Seitenlänge
# farbe: Farbe der Linien
class QuadratV1():
    def __init__(self, fenster, x, y, laenge, farbe="black"):
        self.fenster = fenster
        self.x = x
        self.y = y
        self.farbe = farbe
        self.laenge = laenge
        
        # umhüllendes Rechteck ( als Differenz zum Nullpunkt)
        hd = math.sqrt(laenge**2 / 2) # halbe Diagonale
        self.x1 = -hd
        self.y1 = -hd
        self.x2 = hd
        self.y2 = hd
        
        # Quadrat zeichnen
        self.figur = fenster.create_polygon(x-hd, y, x, y+hd, x+hd, y, x, y-hd,
                                            width=1, outline = farbe, fill='')
    

class QuadratV2(BewegtesObjekt):
    def __init__(self, fenster, x, y, laenge, farbe="black"):
        # Die Basisklasse nimmt uns einen Teil der Arbeit ab
        BewegtesObjekt.__init__(self,fenster, x, y)
        
        self.farbe = farbe
        self.laenge = laenge
        
        # umhüllendes Rechteck ( als Differenz zum Nullpunkt)
        hd = math.sqrt(laenge**2 / 2) # halbe Diagonale
        self.x1 = -hd
        self.y1 = -hd
        self.x2 = hd
        self.y2 = hd
        
        # Quadrat zeichnen
        self.figur = fenster.create_polygon(x-hd, y, x, y+hd, x+hd, y, x, y-hd,
                                            width=1, outline = farbe, fill='')
        
