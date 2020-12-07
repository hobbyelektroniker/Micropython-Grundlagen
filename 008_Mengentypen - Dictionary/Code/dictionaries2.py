# Ein Dictionary mit vorgegebenen Werten erzeugen
dict1 = {
    "land": "Schweiz",
    "ort": "Bern",
    "einwohner": 140000
}
print(dict1)
print()

# Dictionary vollständig löschen
dict2 = dict1.copy()
#del dict2 # gibt eine Fehlerleldung
print(dict2)

# Alle Elemente löschen
dict2 = dict1.copy()
dict2.clear()
print(dict2)
print()

# Ein einzelnes Element löschen
dict2 = dict1.copy()
dict2.pop("ort")
print(dict2)
print()

# Zuletzt hinzugefügtes Element löschen
dict2 = dict1.copy()
dict2.popitem()
print(dict2)
print()

# Wertepaar hinzufügen
dict2 = dict1.copy()
dict2["kanton"] = "BE"
print(dict2)
print()

# Wertepaar ändern
dict2 = dict1.copy()
dict2["kanton"] = "BS"
dict2["ort"] = "Basel"
print(dict2)
dict2.update({"kanton":"BE","ort":"Bern"})
print()





    
    

    


