from fruitmand import *

gewicht = []

for fruit in fruitmand:
    gewicht.append(fruit['weight'])
print(gewicht)

gewicht.sort(reverse = True)
print(gewicht)

for fruit in fruitmand:
    for gewichten in gewicht:
        if fruit['weight'] == gewichten:
            # pos = gewicht.index(gewichten)
            gewicht[gewicht.index(gewichten)] = {fruit['name'] : gewichten / 1000}

for fruit in gewicht:
    print(f"{fruit} kg")



# for fruit in fruitmand:
#     gewicht.append({fruit['name'] : fruit['weight']})
# print(gewicht)

# index_zero = -1
# if 0 in gewicht:
#     index_zero = gewicht.index(0)

# for fruit in fruitmand:
#     adjusted_weight = fruit['weight'] / 1000
#     if fruit['weight'] != 0:
#         print(f"{fruit['name']} {adjusted_weight}kg")
#     else:
#         index_zero / 1000