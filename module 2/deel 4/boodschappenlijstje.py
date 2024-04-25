boodschappenlijst = {}

while True:

    item = input("Welk artikel wilt u toevoegen?: ").lower()

    aantal = int(input(f"Hoeveel {item} wilt u toevoegen?: "))

    if item in boodschappenlijst:
        boodschappenlijst[item] += aantal
    else:
        boodschappenlijst.update({item: aantal})

    print(boodschappenlijst)

    keuze = input("Wilt u nog een artikel toevoegen?: ")
    if keuze == "nee":
        break

print("Dit is uw boodschappenlijst: ")

# for boodschap in boodschappenlijst:
#     for key, value in boodschap.items():
#         print(f"{key} {value}")

print("-[ BOODSCHAPPENLIJST ]-")
for item in boodschappenlijst:
    print(f'{boodschappenlijst[item]}x {item}')
print('----------------------')