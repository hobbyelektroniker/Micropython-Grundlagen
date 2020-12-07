# Ein Dictionary mit vorgegebenen Werten erzeugen
dict1 = {
    "land": "Schweiz",
    "ort": "Bern",
    "einwohner": 140000
}
print(dict1)
print()

# Leeres Dictionary erzeugen 
dict2 = dict()
print(dict2)
print()

# Aus einem anderen Dictionary erzeugen 
dict3 = dict1.copy()
print(dict3)
print()
dict4 = dict(dict1)
print(dict4)
print()

# Aus einer Keyliste (Tupel) erzeugen
dict2 = dict.fromkeys(("land","ort"))
print(dict2)
dict2 = dict.fromkeys(("land","ort"),"default")
print(dict2)
print()

# Einzelnen Wert auslesen
print(dict1["ort"]) # gibt Fehlermeldung, wenn key nich existiert
print()
print(dict1.get("ort"))
print(dict1.get("existiert nicht")) # gibt None zurück
print(dict1.get("existiert nicht","Standardwert"))

# Existiert ein Schlüssel
print("ort" in dict1)
print()

# Alle Schlüssel auflisten
for x in dict1:
    print(x)
print()
for x in dict1.keys():
    print(x)
print()

# Alle Werte auflisten
for x in dict1.values():
    print(x)
print()

# Alle Wertepaare auflisten
for k,v in dict1.items():
    print(k,v)
print()

# Anzahl Wertepaare
print(len(dict1))
print()





    
    

    


