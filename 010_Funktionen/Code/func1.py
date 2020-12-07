def flaeche(a, b):
    rechtecksflaeche = a * b    # Rechteck mit den Seiten a und b
    dreiecksflaeche = a * b / 2 # Dreieck mit Grundlinie a und Höhe b
    return rechtecksflaeche, dreiecksflaeche
        
a = 3
b = 5

resultat = flaeche(a,b) # Gibt Tupel zurück
print(resultat)
print(resultat[1])

rechteck, dreieck = flaeche(a, b) # Direkte Zuweisung
print("Das Rechteck mit den Seitenlängen {} cm und {} cm hat die Fläche {} cm2.".format(a,b,rechteck))
print("Das Dreieck mit der Grundlinie {} cm und der Höhe {} cm hat die Fläche {} cm2.".format(a,b,dreieck))


