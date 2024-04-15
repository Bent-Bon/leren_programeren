boodschappenlijst = []

while True:

    item = input("Welk artikel wilt u toevoegen?: ").lower()

    aantal = int(input(f"Hoeveel {item} wilt u toevoegen?: "))

    for boodschap in boodschappenlijst:
        if item in boodschap:
            boodschap[item] += aantal
            break
    else:
        boodschappenlijst.append({item: aantal})

    print(boodschappenlijst)

    keuze = input("Wilt u nog een artikel toevoegen?: ")
    if keuze == "nee":
        break

print("Dit is uw boodschappenlijst: ")

for boodschap in boodschappenlijst:
    for key, value in boodschap.items():
        print(f"{key} {value}")