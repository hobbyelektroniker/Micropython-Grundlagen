# Blöcke

"""
Wir beschäftigen uns
hier mit Blöcken
am Beispiel einer Funktion
"""

def addiere(a,b): # Mit dem : wird der Block eingeleitet
    c = a + b     # Nach dem : wird eingerückt
    print(c)      # Diese Einrückung bleibt für alle Befehle
                  # innerhalb des Blockes erhalten
    
# Keine Einrückung mehr, damit gehört dieser Code nicht mehr zur Funktion
print("Start")
addiere(3,5)
print("Ende")

