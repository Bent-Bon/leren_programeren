from fruitmand import *
kleurlijst = []

for fruit in fruitmand:
    if fruit["name"] == "druif":
        del fruitmand[fruitmand.index(fruit)]
    elif fruit["color"] not in kleurlijst:
        kleurlijst.append(fruit["color"])
        print(fruit["color"])
print(fruitmand)