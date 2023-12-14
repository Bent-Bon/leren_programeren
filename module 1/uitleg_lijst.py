klas = []
for _ in range(3):
    persoon = {}

    persoon["naam"] = input("wat is uw naam?: ")
    persoon["tussenvoegsel"] = input("wat is uw tussenvoegsel?: ")
    persoon["achternaam"] = input("wat is uw achter naam?: ")
    persoon["leeftijd"] = input("wat is uw leeftijd?: ")
    klas.append(persoon)

print(klas)
print(klas[1]["leeftijd"])