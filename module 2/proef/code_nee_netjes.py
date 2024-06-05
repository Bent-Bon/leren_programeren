import random
import time
import os
namen_lijst = ["a", "b", "c"]
lootjes_dict = {}

# while True:
#     naam = input("geef een naam: ")
# 
#     if naam not in namen_lijst:
#         namen_lijst.append(naam)
#     else:
#         print("deze naam is al in de lijst")
#         continue
# 
#     if len(namen_lijst) >= 3:
#         again = input("wil je nog een naam toevoegen?: ")
#         if again.lower() == "nee":
#             break

namen_lijst_backup = namen_lijst.copy()
random.shuffle(namen_lijst)

for i in range(len(namen_lijst)):
    lootjes_dict[namen_lijst[i]] = namen_lijst[(i + 1) % len(namen_lijst)]

while True:
    name_reveal = input("welke naam wil je weten?: ")
    if name_reveal in namen_lijst:
        print(f"{lootjes_dict[name_reveal]}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif name_reveal == "nee":
        break
    else:
        print("deze naam is niet in de lijst")