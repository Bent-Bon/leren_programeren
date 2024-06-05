from collections import Counter
import math, random

def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}

    # Gemiddelde berekenen
    aantal = len(getallen)

    # Som van alle getallen in de lijst
    som = sum(getallen)

    # Gemiddelde berekenen
    gemiddelde = som / aantal

    # Het grootste getal in de lijst
    grootste_getal = max(getallen)
    
    # Het kleinste getal in de lijst
    kleinste_getal = min(getallen)
    
    # Het eerste getal in de lijst
    eerste_getal = getallen[0]
    
    # Het kleinste getal gedeeld door het eerste controle getal
    delen1 = kleinste_getal / controlegetal1

    # Het grootste getal gedeeld door het tweede controle getal
    delen2 = grootste_getal / controlegetal2

    # alle unieke getallen
    unieke_getallen = list(set(getallen))

    # Aantal unieke elementen in de lijst
    aantal_unieke_elementen = len(unieke_getallen)

    # Verschil tussen aantal unieke elementen en eerste controle getal
    verschil1 = abs(aantal_unieke_elementen - controlegetal1)

    # Sorteer de lijst van getallen
    gesorteerde_lijst = sorted(getallen)

    # Sorteer de lijst van unieke getallen
    gesorteerde_lijst_uniek = sorted(unieke_getallen)

    # Tel het aantal keren dat elk uniek element voorkomt in de lijst
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer

    # Getallen die deelbaar zijn door het eerste controlle getal
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)

    # Getallen die deelbaar zijn door het tweede controlle getal
    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)

    # Controleer of een bepaald getallen in de lijst voorkomen
    komtvoor = controlegetal1 in getallen and controlegetal2 in getallen

    # Vindt de posities van heteerste controle getal
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)

    # Standaardafwijking berekenen
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)

    # Shuffle de lijst
    random.shuffle(getallen)

    # Pak een random getal uit de lijst
    random_getal = getallen[random.randint(0,aantal-1)]

    # Verschil tussen twee getallen
    verschil2 = abs(random_getal - controlegetal2)

    resultaten = {
        "Aantal getallen": aantal,
        "Gemiddelde": gemiddelde,
        "Som": som,
        "Grootste getal": grootste_getal,
        "Kleinste getal": kleinste_getal,
        "Eerste getal": eerste_getal,
        f"{kleinste_getal} / {controlegetal1}": delen1,
        f"{grootste_getal} / {controlegetal2}": delen2,
        "Aantal unieke elementen": aantal_unieke_elementen,
        f"Het verschil tussen {aantal_unieke_elementen} & {controlegetal1}": verschil1,
        "Gesorteerde lijst getallen": gesorteerde_lijst,
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst_uniek,
        "Telling van elementen": telling_elementen,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": getallen,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")

def aantal(lijst):
    return len(lijst)

def som(lijst):
    return sum(lijst)

def gemiddelde(lijst):
    return sum(lijst) / len(lijst)

def grootste_getal(lijst):
    return max(lijst)

def kleinste_getal(lijst):
    return min(lijst)

def eerste_getal(lijst):
    return lijst[0]

def kleinste_getal_delen(lijst, number):
    return kleinste_getal(lijst) / number

def grootste_getal_delen(lijst, number):
    return grootste_getal(lijst) / number

def alle_unieke_getallen(lijst):
    return list(set(lijst))

def aantal_unieke_elementen(lijst):
    return len(alle_unieke_getallen(lijst))

def Verschil_unieke_elementen_controle_getal(lijst, getal):
    return abs(aantal_unieke_elementen(lijst) - getal)

def Sorteer_lijst(lijst):
    return sorted(lijst)

def Sorteer_lijst_unieke_getallen(lijst):
    return sorted(alle_unieke_getallen(lijst))

def aantal_unieke_element_in_lijst(lijst):
    telling_elementen = {}
    for getal in lijst:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

def Getallen_deelbaar_eerste_controlle_getal(lijst, getal):
    deelbaar1 = []
    for number in alle_unieke_getallen(lijst):
        if number % getal == 0:
            deelbaar1.append(number)
    return sorted(deelbaar1)

def Getallen_deelbaar_tweede_controlle_getal(lijst, getal):
    deelbaar2 = []
    for getal in alle_unieke_getallen(lijst):
        if getal % getal== 0:
            deelbaar2.append(getal)
    return sorted(deelbaar2)

def controleer_getallen_in_lijst(lijst, getal1, getal2):
    return getal1 in lijst and getal2 in lijst

def posities_eerste_controle_getal(lijst, getal):
    posities = []
    for index, num in enumerate(lijst):
        if num == getal:
            posities.append(index)
    return posities

def Standaardafwijking_berekenen(lijst):
    verschil_kwadraat = sum((x - gemiddelde(lijst)) ** 2 for x in lijst)
    variantie = verschil_kwadraat / aantal(lijst)
    return math.sqrt(variantie)

def Shuffle(lijst):
    return random.shuffle(lijst)

def random_getal(lijst):
    return lijst[random.randint(0,aantal(lijst)-1)]

def Verschil_twee_getallen(lijst, getal):
    return abs(random_getal(lijst) - getal)