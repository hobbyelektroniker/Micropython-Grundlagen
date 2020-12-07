def ich_zeige_was_ich_bekomme(a,b,*args, c=2,d=3, **kwargs):
    print("Positionsargumente: {}, {}, {}".format(a,b,args))
    print("Standardargumente: {}, {}".format(c,d))
    print("Keywordargumente: {}".format(kwargs))
    print()
    
ich_zeige_was_ich_bekomme(1,2)
ich_zeige_was_ich_bekomme(1,2,3,4)
ich_zeige_was_ich_bekomme(1,2,3,4,d=5)
ich_zeige_was_ich_bekomme(1,2,3,4,c=5,e=12,text="Ein Text")


