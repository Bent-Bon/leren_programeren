import random

namen_lijst = ["a", "b", "c"]
lootjes_dict = {}

# Uncomment this block if you want to take user input
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

for x in range(1000):
    random.shuffle(namen_lijst)
    for i in range(len(namen_lijst)):
        lootjes_dict[namen_lijst[i]] = namen_lijst[(i + 1) % len(namen_lijst)]

    print(lootjes_dict)

    print("")
    for naam, loot in lootjes_dict.items():
        if naam == loot:
            print("error")
            quit()
        else:
            lootjes_dict.clear()
            break