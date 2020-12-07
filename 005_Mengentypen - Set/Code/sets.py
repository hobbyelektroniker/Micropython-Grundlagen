# Ein Set mit vorgegebenen Werten erzeugen
set1 = {"Hallo",3,1.25,"Welt"}
print(set1)

# Ein leeres Set erzeugen
set2 = set()
print(set2)

# Elemente zum Set hinzufügen
set2.add("neu")
set2.add("Hallo")
set2.add(5)
print(set2)

# Ein Set aus einem anderen Set erzeugen
set3 = set1.copy()
print(set3)

# Ein Set aus zwei anderen Sets erzeugen
set3 = set1.union(set2)
print(set3)

# Einen Generator verwenden
set3 = set(range(1,5))
print(set3)



# Abfragen, ob ein Element vorhanden ist
print("Hallo" in set1)
print("Hello" in set1)

# Alle Elemente auflisten
for x in set1:
    print(x)
    
# Anzahl Elemente im Set
print(len(set1))

# Im ersten Set enthalten, im zweiten nicht
print()
print("------- difference -------")
set1 = {"Hallo",3,1.25,"Welt"}
set2 = {"Hallo",3,"Jahr 2020",5}
print("Set1: " + str(set1))
print("Set2: " + str(set2))
print(set1.difference(set2))

# Nur in einem der beiden Sets enthalten
print()
print("------- symmetric_difference -------")
set1 = {"Hallo",3,1.25,"Welt"}
set2 = {"Hallo",3,"Jahr 2020",5}
print("Set1: " + str(set1))
print("Set2: " + str(set2))
print(set1.symmetric_difference(set2))

# Gemeinsamkeiten zwischen zwei Sets
print()
print("------- intersection -------")
set1 = {"Hallo",3,1.25,"Welt"}
set2 = {"Hallo",3,"Jahr 2020",5}
print("Set1: " + str(set1))
print("Set2: " + str(set2))
print(set1.intersection(set2))


# Ein Set enthält das Andere
print()
print("------------------------")
set1 = {"Hallo",3,1.25,"Welt"}
set2 = {"Hallo",3,"Jahr 2020",5}
set3 = {"Hallo","Welt"}
print("Set1: " + str(set1))
print("Set2: " + str(set2))
print("Set3: " + str(set3))
print("------- issubset -------")
print("Set3 ist Subset von Set1: " + str(set3.issubset(set1)))
print("Set1 ist Subset von Set3: " + str(set1.issubset(set3)))
print("------- issuperset -------")
print("Set3 ist Superset von Set1: " + str(set3.issuperset(set1)))
print("Set1 ist Superset von Set3: " + str(set1.issuperset(set3)))

# Gibt es keine Gemeinsamkeit
print()
print("------- isdisjoint -------")
set1 = {"Hallo",3,1.25,"Welt"}
set2 = {"Hallo",3,"Jahr 2020",5}
set3 = {"Welt",2020}
print("Set1: " + str(set1))
print("Set2: " + str(set2))
print("Set3: " + str(set3))
print("Set1 hat keine gemeinsamen Elemente mit Set 3: " + str(set1.isdisjoint(set3)))
print("Set2 hat keine gemeinsamen Elemente mit Set 3: " + str(set2.isdisjoint(set3)))

print()

# Set vollständig löschen
del set3
# print(set3) gibt Fehler

# Set leeren
set2.clear()
print(set2)

# Elemente entfernen
set1.remove("Hallo") # "Hallo" muss existieren
print(set1)
#set1.remove("Hallo") würde einen Fehler geben
set1.discard("Welt") # "Welt" muss nicht existieren
set1.discard(2)
print(set1)

# Einzelne Elemente hizufügen
set1.add("Hallo")
print(set1)

# Ein Set einem Set hinzufügen
#set1.add({1,2,3}) geht nicht
set1.update({1,2,3})
print(set1)
set2 = {"Hallo",3,"Jahr 2020",5}
set1.update({1,2,3})
print(set1)

# Berechnungen
print()
print("------- Berechnungen -------")
set1 = {"Hallo",3,1.25,"Welt"}
set2 = {"Hallo",3,"Jahr 2020",5}
print("Set1: " + str(set1))
print("Set2: " + str(set2))

# Im ersten Set enthalten, im zweiten nicht
set1.difference_update(set2)
print("difference_update: " + str(set1))


# Nur in einem der beiden Sets enthalten
set1 = {"Hallo",3,1.25,"Welt"}
set2 = {"Hallo",3,"Jahr 2020",5}
set1.symmetric_difference_update(set2)
print("symmetric_difference_update: " + str(set1))

# Gemeinsamkeiten zwischen zwei Sets
set1 = {"Hallo",3,1.25,"Welt"}
set2 = {"Hallo",3,"Jahr 2020",5}
set1.intersection_update(set2)
print("intersection_update: " + str(set1))
