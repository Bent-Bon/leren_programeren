import random
namen_lijst = []

while True:
    naam = input("geef een naam: ")

    if naam not in namen_lijst:
        namen_lijst.append(naam)
    else:
        print("deze naam is al in de lijst")
        continue

    if len(namen_lijst) >= 3:
        again = input("wil je nog een naam toevoegen?: ")
        if again.lower() == "nee":
            break

for naam in namen_lijst[::]:
    while True:
        ran = random.choice(namen_lijst)
        if ran != naam and type(ran) != dict:
            break
    namen_lijst.append({naam : ran})
    namen_lijst.remove(ran)
print(namen_lijst)