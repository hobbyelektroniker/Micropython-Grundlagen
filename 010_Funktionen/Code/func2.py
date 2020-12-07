def laenge(a, b, *args):
    print()
    print(args)
    total = a+b
    for i in args:
        total += i
    return total

print(laenge(2,3))
print(laenge(2,3,4,10))