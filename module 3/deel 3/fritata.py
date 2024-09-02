import math

ingredienten = {
    "ei" : 7,
    "melk" : 120, #ml
    "zout" : 0.5, #g
    "peper" : 0.25, #g
    "olie" : 10, #g
    "ui" : 1,
    "knoflook" : 1,
    "paprika" : 1,
    "spinazie" : 240, #g
    "kaas" : 120 #g
}

mensen = int(input("Voor hoeveel mensen maak je het?: "))

def round_special(value):
    return round(value * 4) / 4

for ingredient in ingredienten:
    if ingredient in ["melk", "zout", "peper", "olie", "spinazie", "kaas"]:
        unit = "ml" if ingredient == "melk" else "g"
        updated_quantity = round_special((ingredienten[ingredient] / 4) * mensen)
    else:
        unit = ""
        updated_quantity = math.ceil((ingredienten[ingredient] / 4) * mensen)
    
    ingredienten[ingredient] = f"{updated_quantity} {unit}".strip()

# To check the updated values
print(ingredienten)