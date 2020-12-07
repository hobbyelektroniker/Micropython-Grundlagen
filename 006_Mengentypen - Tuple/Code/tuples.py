# Ein Tuple mit vorgegebenen Werten erzeugen
tup1 = ("Hallo",3,1.25,"Welt",2,3,4,5)
print(tup1)
print()

# Leeres Tuple erzeugen 
tup2 = tuple() # macht nicht viel Sinn !!!
print(tup2)
print()

# Aus anderen Collections erzeugen
set1 = {"Hallo",3,1.25,"Welt"}
tup2 = ("Hallo",3,"Jahr 2020",5)
tup1 = tuple(set1)
print(tup1)
tup3 = tup2
print(tup3)
tup3 = tup1 + tup3
print(tup3)
print()

# Mit Hilfe eines Generators erzeugen
tup1 = tuple(range(1,5))
print(tup1)
print()

# Abfragen, ob ein Element vorhanden ist
tup1 = (3,"Hallo",3,"Hallo","Welt",2,4,5)
print("Hallo" in tup1)
print("Hello" in tup1)
print()

# Alle Elemente auflisten
for x in tup1:
    print(x)
print()

# Anzahl Elemente im Tuple
print(len(tup1))
print()

# Einzelnes Element auslesen
print(tup1[3])
print()

# Wieviele Male kommt ein Wert vor
print(tup1.count("Hallo"))
print()

# Welcher Index hat das erste Vorkommen eines Wertes
print(tup1.index("Hallo")) # Der Wert muss existieren!!!
print()

# Das erste und das letzte Element
tup1 = (3,"Hallo",3,"Hallo","Welt",2,4,5)
print(tup1)
print(tup1[0])
print(tup1[-1])
print()

# Der Anfang und das Ende
tup1 = (3,"Hallo",3,"Hallo","Welt",2,4,5)
print(tup1)
print(tup1[:3]) # Element 0 bis 2
print(tup1[4:]) # Element 4 bis Ende
print()

# Ein Bereich aus der Mitte
tup1 = (3,"Hallo",3,"Hallo","Welt",2,4,5)
print(tup1)
print(tup1[2:5])   # Element 2 bis 4
print(tup1[-3:-1]) # Drittletztes Element bis zweitletztes Element

# Tuple vollständig löschen
del tup1
# print(tup1) gibt Fehler

    