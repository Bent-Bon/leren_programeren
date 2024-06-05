import random
namen_lijst = ["a", "b", "c"]
loostjes_lijst = []

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
for x in range(1000): # testen van code

    for naam in namen_lijst:
        for naam_pos_for in range(len(namen_lijst)):
            ran = random.choice(namen_lijst)
            if ran != naam:
                break
        loostjes_lijst.append({naam : ran})
    print(loostjes_lijst)

# testen van code
    print("")
    loostjes_lijst.clear()
    for lootje in loostjes_lijst:
        for naam, loot in lootje.items():
            if naam == loot:
                print("error")
                quit()