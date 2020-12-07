x = 0
while x < 6:
    x += 1
    y = 2 * x
    print(x,y)

print("-------")

x = 0
while x < 6:
    x += 1
    y = 2 * x
    print(x,y)
    if (x == 3): break

print("-------")

x = 0
while True:
    x += 1
    y = 2 * x
    print(x,y)
    if (x > 5): break
print("-------")

x = 0
while x < 6:
    x += 1
    if (x == 3): continue
    y = 2 * x
    print(x,y)

print("-------")

x = 0
while x < 6:
    x += 1
    if (x == 3): continue
    y = 2 * x
    print(x,y)
else:
    print("Jetzt sind wir fertig!")
print("Das war's.")


    