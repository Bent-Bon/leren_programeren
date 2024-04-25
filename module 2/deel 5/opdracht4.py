from fruitmand import *
import random
aantal = int(input("noem een nummer: "))

for x in range(aantal):
    item = random.choice(fruitmand)
    print(item["name"])