# Eine List mit vorgegebenen Werten erzeugen
list1 = ["Hallo",3,1.25,"Welt",2,3,4,5]
print(list1)
print()

# Leere List erzeugen 
list2 = list()
list3 = []
print(list2)
print(list3)
print()

# Aus anderen Collections erzeugen
set1 = {"Hallo",3,1.25,"Welt"}
list1 = list(set1)
print(list1)

list2 = ["Hallo",3,"Jahr 2020",5]
list3 = list2.copy()
list4 = list(list2)
print(list3)
print(list4)

list1 = ["Hallo",3,1.25,"Welt"]
list2 = ["Hallo",3,"Jahr 2020",5]
list3 = list2 # Das erzeugt keine neue Liste!!!
print(list3)
list3[1] = 7
print(list2)

list1 = ["Hallo",3,1.25,"Welt"]
list2 = ["Hallo",3,"Jahr 2020",5]
list3 = list1 + list2
print(list3)
print()

# Mit Hilfe eines Generators erzeugen
list1 = list(range(1,5))
print(list1)
print()

# Abfragen, ob ein Element vorhanden ist
list1 = [3,"Hallo",3,"Hallo","Welt",2,4,5]
print("Hallo" in list1)
print("Hello" in list1)
print()

# Alle Elemente auflisten
for x in list1:
    print(x)
print()

# Anzahl Elemente in List
print(len(list1))
print()

# Einzelnes Element auslesen
print(list1[3])
print()

# Wieviele Male kommt ein Wert vor
print(list1.count("Hallo"))
print()

# Welcher Index hat das erste Vorkommen eines Wertes
print(list1.index("Hallo")) # Der Wert muss existieren!!!
print()

# Das erste und das letzte Element
list1 = [3,"Hallo",3,"Hallo","Welt",2,4,5]
print(list1)
print(list1[0])
print(list1[-1])
print()

# Der Anfang und das Ende
list1 = [3,"Hallo",3,"Hallo","Welt",2,4,5]
print(list1)
print(list1[:3]) # Element 0 bis 2
print(list1[4:]) # Element 4 bis Ende
print()

# Ein Bereich aus der Mitte
list1 = [3,"Hallo",3,"Hallo","Welt",2,4,5]
print(list1)
print(list1[2:5])   # Element 2 bis 4
print(list1[-3:-1]) # Drittletztes Element bis zweitletztes Element
print()

# List vollständig löschen
del list1
# print(list1) gibt Fehler

# Alle Elemente der List löschen
list1 = [3,"Hallo",3,"Hallo","Welt",2,4,5]
print(list1)
list1.clear()
print(list1)
print()

# Einzelne Elemente löschen
list1 = [3,"Hallo",3,"Hallo","Welt",2,4,5]
print(list1)
list1.remove("Hallo") # Hallo muss existieren, löscht das erste Vorkommen 
print(list1)
list1.pop() # löscht das letzte Element
print(list1)
list1.pop(2) # löscht das Element mit Index 2
print(list1)
print()

# Elemente hinzufügen
list1 = [3,"Hallo"]
list2 = ["Welt","Hello"]
print(str(list1) + "     " + str(list2))

list1.append("Hi")
print(list1)

list1.insert(2,"neu")
print(list1)

list1.append(list2)
print(list1)
print()

list1 = [3,"Hallo"]
print(list1)
list1.extend(["Welt","Hello"])
print(list1)

# Reihenfolge umkehren
list1 = [3,"Hallo",3,"Hallo","Welt",2,4,5]
print(list1)
list1.reverse()
print(list1)
print()

# Sortierung, geht nur bei gleichen Typen
list1 = [3,5,2,5,4]
print(list1)
list1.sort()
print(list1)
print()

list1 = ["Kirsche","Banane","Apfel"]
print(list1)
list1.sort()
print(list1)
print()

list1 = [3,"Hallo",3,"Hallo","Welt",2,4,5]
print(list1)
#list1.sort() # geht nicht!!!
print(list1)
print()












