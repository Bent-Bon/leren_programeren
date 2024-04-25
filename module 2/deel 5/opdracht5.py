from fruitmand import *
fruitlijst = []

for fruit in fruitmand:
    fruitlijst.append(fruit["name"])

print(fruitlijst)
fruitlijst.reverse()
print(fruitlijst)