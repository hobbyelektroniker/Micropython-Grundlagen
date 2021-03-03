'''
  Objektorientiert Programmierung
  Ein Klasse für ein bewegtes Objekt
    
  Version 1.00, 27.02.2021
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Der Code kann mit Quellenangabe frei verwendet werden.
'''

# Bewegtes Objekt

# Diese Klasse zeichnet eine geometrische Figur dar, die sich bewegen kann
# Als einfaches Beispiel wird eine kleine Scheibe verwendet
# fenster: das Fenster, in dem das Objekt gezeichnet werden soll
# x, y: x und y Koordinaten des Mittelpunkts
class BewegtesObjektV1():
    def __init__(self, fenster, x, y):
        self.fenster = fenster
        self.x = x
        self.y = y

        # Am Anfang soll sich noch nichts bewegen
        self.moveX = 0
        self.moveY = 0
        
        # Die Scheibe wird angezeigt
        self.figur = fenster.create_oval(x-10, y-10, x+10, y+10, width=1, outline="green", fill = "green")
        
    # Die Figur soll sich in die angegebene Richtung bewegen    
    def bewegung(self, x=0, y=0):
        self.moveX = x
        self.moveY = y
        self.bewege()
        
    # Ein einzelner Bewegungsschritt wird durchgeführt
    def bewege(self):
        # Die Figur wird bewegt und an der neuen Position angezeigt
        self.fenster.move(self.figur, self.moveX, self.moveY)
        self.fenster.update()
        
        
# In Version 2 wird keine Beispielfigur mehr erzeugt
# Von dieser Klasse darf keine alleinstehende Instanz mehr erstellt werden
class BewegtesObjektV2():
    def __init__(self, fenster, x, y):
        self.fenster = fenster
        self.x = x
        self.y = y

        # Am Anfang soll sich noch nichts bewegen
        self.moveX = 0
        self.moveY = 0
        
        # Keine Figur definiert
        self.figur = None
        
    # Die Figur soll sich in die angegebene Richtung bewegen    
    def bewegung(self, x=0, y=0):
        self.moveX = x
        self.moveY = y
        self.bewege()
        
    # Ein einzelner Bewegungsschritt wird durchgeführt
    def bewege(self):
        # Die Figur wird bewegt und an der neuen Position angezeigt
        self.fenster.move(self.figur, self.moveX, self.moveY)
        self.fenster.update()
        

# Version 3 steuert die Animation so, dass die Figur immer innerhalb des Fensters bleibt
class BewegtesObjektV3():
    def __init__(self, fenster, x, y):
        self.fenster = fenster
        self.x = x
        self.y = y
        
        # Wir müssen die Abmessungen des Fensters kennen
        fenster.update()
        self.maxY = fenster.winfo_height()
        self.maxX = fenster.winfo_width()

        # Am Anfang soll sich noch nichts bewegen
        self.moveX = 0
        self.moveY = 0
        
        # Keine Figur definiert
        self.figur = None
        
    # Die Figur soll sich in die angegebene Richtung bewegen    
    def bewegung(self, x=0, y=0):
        self.moveX = x
        self.moveY = y
        self.bewege()
        
    # Ein einzelner Bewegungsschritt wird durchgeführt
    def bewege(self):
        # Es wird berechnet, wo die nächste Position hinkommen würde
        x = self.x + self.moveX
        y = self.y + self.moveY        
        
        # Falls wir ausserhalb des Spielfeldes wären, stoppen wir rechtzeitig
        # Für das nächste Mal wird die Richtung umgekehrt
        if (x + self.x1 < 0):
            x = -self.x1
            self.moveX = -self.moveX
        if (x + self.x2 > self.maxX):
            x = self.maxX - self.x2
            self.moveX = -self.moveX
        if (y + self.y1 < 0):
            y = -self.y1
            self.moveY = -self.moveY
        if (y + self.y2 > self.maxY):
            y = self.maxY - self.y2
            self.moveY = -self.moveY
        
        # Die korrigierte Bewegung wird ausgeführt und die neuen Koordinaten werden gespeichert    
        self.fenster.move(self.figur, x-self.x, y-self.y)
        self.x = x
        self.y = y
        self.fenster.update()
        
        
        