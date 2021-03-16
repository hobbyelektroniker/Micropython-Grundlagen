'''
  Objektorientiert Programmierung
  Eine Kreisklasse
    
  Version 1.10, 15.03.2021
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

# Kreis
from bewegt_klasse import BewegtesObjektV3 as BewegtesObjekt

# Diese Klasse zeichnet einen Kreis
# fenster: das Fenster, in dem der Kreis gezeichnet werden soll
# x, y: x und y Koordinaten des Mittelpunkts
# radius: Radius des Kreises
# farbe: Farbe der Kreislinie
class KreisV1():
    def __init__(self, fenster, x, y, radius, farbe = 'black'):
        self.fenster = fenster
        self.x = x
        self.y = y
        self.farbe = farbe
        self.radius = radius
        
        # umhüllendes Rechteck ( als Differenz zum Nullpunkt)
        self.x1 = -radius
        self.y1 = -radius
        self.x2 = radius
        self.y2 = radius
        
        # Kreis zeichnen
        self.figur = fenster.create_oval(x-radius, y-radius, x+radius, y+radius,
                                         width=1, outline=farbe, fill = '')
        

# Version 2 verwendet als Basisklasse die Klasse BewegtesObjekt
class KreisV2(BewegtesObjekt):
    def __init__(self, fenster, x, y, radius, farbe = 'black'):
        # Die Basisklasse nimmt uns einen Teil der Arbeit ab
        BewegtesObjekt.__init__(self,fenster, x, y)        

        self.farbe = farbe
        self.radius = radius
        
        # umhüllendes Rechteck ( als Differenz zum Nullpunkt)
        self.x1 = -radius
        self.y1 = -radius
        self.x2 = radius
        self.y2 = radius
        
        # Kreis zeichnen
        self.figur = fenster.create_oval(x-radius, y-radius, x+radius, y+radius,
                                         width=1, outline=farbe, fill = '')
