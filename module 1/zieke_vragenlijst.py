PASO = 0
ECO = 0

zieke_lijst_p2 = []


rijbewijs = str(input("heb je een ce rijbewijs?: "))
if rijbewijs == "nee":
    zieke_lijst_p2.append("u heeft geen rijbewijs voor de vrachtwagen")
else:
    pass

hoed = str(input("heb je een hoge hoed?: "))
if hoed == "nee":
    zieke_lijst_p2.append("u heeft geen hogehoed")
else:
    pass

zwaar = int(input("hoe zwaar ben je?: "))
if zwaar >= 90 and zwaar <= 120:
    ECO = 9
elif zwaar < 90:
    telicht = 90 - zwaar
    zieke_lijst_p2.append(f"u bent {telicht}㎏ te licht")
else:
    tezwaar = zwaar - 120
    zieke_lijst_p2.append(f"u bent {tezwaar}㎏ te zwaar")

ervaring = str(input("heb je 4 jaar of meer aan dieren dressuren praktijk ervaring?: "))
if ervaring == "nee":
    longleren = str(input("heb je 5 jaar of meer jongleer ervaring?: "))
    if longleren == "ja":
        jaren_b = str(input("hoeveel jaar ervaring?: "))
        PASO = 9
    else:
        zieke_lijst_p2.append("u kan niet longleren en u heeft niet genoeg ervaring op het")
elif ervaring == "ja":
    jaren_a = str(input("hoeveel jaar ervaring?: "))
    PASO = 9

gender = str(input("welke gender ben je?: "))
if gender == "man":
    snor = str(input("heb je een snor?: "))
    if snor == "nee":
        zieke_lijst_p2.append("u heeft geen snor")
    else:
        pass
elif gender == "vrouw":
    haar = str(input("heb je rood krullig haar?: "))
    if haar == "nee":
        zieke_lijst_p2.append("u heeft geen rood krullig haar")
    else:
        pass
else:
    lach = str(input("heb je een bredelach?: "))
    if lach == "nee":
        zieke_lijst_p2.append("u heeft geen glimlach")
    else:
        pass

if rijbewijs == "ja" and hoed == "ja" and PASO == 9 and ECO == 9 and (snor == "ja" or haar == "ja" or lach == "ja") :
    print("u bent aan genomen")
else:
    print(f"u bent niet aan genomen omdat")

for item in zieke_lijst_p2:
    print(item)