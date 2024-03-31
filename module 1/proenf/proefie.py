import random

duik_deur = 0
raam_deur = 0

print("je loopt een griezelige tuin")
print("in die tuin zie je een vervloekt huis staan")
print("je ziet dat er een raam is open gebroken is en je ziet ook dat het slot van de deur is open gebroken")
huis = input("hoe ga je naar binnen het raam of de deur? (raam/deur): ").lower()

if huis == "deur":
    print("je duwt de deur open")
    print("vervolgens komt er een zwaard op je af")
    duikt = input("welke kant duik je op naar links of naar rechts: ").lower()
    ran = random.randint(1, 2)
    if ran == 1:
        print("het zwaard raakt je recht in je hoofd")
        print("je was te laat...")
        print("game over")
        exit()
    else:
        if duikt == "links":
            print("je ontwijkt net het zwaard en duikt naar links een kamer in")
            duik_deur = 1
        else:
            print("je ontwijkt net het zwaard en duikt naar rechts een kamer in")
else:
    duik_deur = 1
    print("je kruipt voorzichtig door het raam")
if duik_deur == 1:
    print("je staats nu in een donkere kamer")
    print("je zoekt naar iets van licht")
    print("na eventjes zoeken vind je een soort iets wat als een licht knopje zou kunnen voelen")
    print("net toen je het knopjes wou gebruiken komt er uit het niks een heel fel wit licht van uit het plafond")
    print("en je ziet dat wat in je hand is geen licht knopje is maar een heilig kruis")
    print("je hoord een luide stem zeggen gij die deze villa betreed vrij mijn ziel en gij zal beloond worden")
    print("je ziet vervolgens 2 deuren ")
    raam_deur = 