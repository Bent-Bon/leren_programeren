import random
namen_lijst = ["a", "b", "c", "d", "e", "f"]
loostjes_lijst = {}

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

for naam in namen_lijst[::]:
    for naam_pos_for in range(len(namen_lijst)):
        ran = random.choice(namen_lijst)
        if ran != naam:
            break
    loostjes_lijst[naam] = ran

while True:
    name_reveal = input("welke naam wil je weten?: ")
    if name_reveal in namen_lijst:
        print(f"loostjes_lijst[name_reveal]")
        break