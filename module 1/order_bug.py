def vraag_getal(aantal):
    getal = int(input("Voer het " + aantal + " getal in: "))
    return getal

def deel_getallen(a, b):
        resultaat = a / b
        return resultaat

getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")

if getal_1 != 0 and getal_2 != 0:
    
    resultaat = deel_getallen(getal_1, getal_2) 
    print(f"{getal_1} gedeeld door {getal_2} is gelijk aan {resultaat}")
else:
     print("Kan niet delen door 0")