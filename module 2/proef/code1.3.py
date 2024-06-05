import random
namen_lijst = ["a", "b", "c"]
lootjes_dict = {}

# while True:
#     naam = input("geef een naam: ")

#     if naam not in namen_lijst:
#         namen_lijst.append(naam)
#     else:
#         print("deze naam is al in de lijst")
#         continue

#     if len(namen_lijst) >= 3:
#         again = input("wil je nog een naam toevoegen?: ")
#         if again.lower() == "nee":
#             break

namen_lijst_backup = namen_lijst.copy()
counter = 0

for naam in namen_lijst[::]:
    while True:
        ran = random.choice(namen_lijst)
        if ran != naam and type(ran) != dict:
            break
        if counter >= 3:
            lootjes_dict.clear()
            namen_lijst = namen_lijst_backup.copy()
            counter = 0

    lootjes_dict[naam] = ran
    namen_lijst.remove(ran)
print(namen_lijst)