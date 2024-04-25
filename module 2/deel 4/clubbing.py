from clubbing_voorbeeld import *

stempel = False
x = False
bandje = False

leeftijd = int(input("how old are you?: "))
age_18 = 18 - leeftijd
age_21 = 21 - leeftijd

if leeftijd < 18:
    print("je mag niet naar binnen")
    print(f"probeer het in {age_18} jaar nog eens")
    exit()
else:
    naam = input("wat is je naam?: ")
    if naam in VIP_LIST:
        if leeftijd >= 21:
            bandje = "blauw"
        else:
            bandje = "rood"
        print(f"je krijgt een {bandje} bandje van mij")
    else:
        if leeftijd >= 21:
            stempel = True
            print("je krijgt een stempel")
    print(DRANKJES)
    drinken = input("wat wil je drinken?: ").lower()

    if drinken == "bier":
        prijs = PRIJS_BIER
    elif drinken == "cola":
        prijs = PRIJS_COLA
    elif drinken == "champagne":
        prijs = PRIJS_CHAMPAGNE

    eind_normaal = f"alsjeblieft je {drinken}, dat is dan €{prijs}"

    if drinken in DRANKJES:
        if drinken == "bier" or drinken == "cola":
                if drinken == "bier" and stempel == True or bandje == "rood" or bandje == "blauw":
                    if bandje == "rood" or bandje == "blauw":
                        print("alstublieft complimenten van het huis")
                        exit()
                    else:
                        print(eind_normaal)
                        exit()
                else:
                    x = True
                    if drinken == "bier":
                        print("sorry je mag geen alcohol bestellen onder 21")
                        print(f"probeer het in {age_21} jaar nog eens")

        if drinken == "champagne" or x == True:
            if bandje == "blauw" or bandje == "rood":
                if bandje == "blauw":
                    print(eind_normaal)
                    exit()
                else:
                    print("sorry je mag geen alcohol bestellen onder 21")
                    print(f"probeer het in {age_21} jaar nog eens")
                    exit()
            else:
                print("sorry alleen vips mogen champagne bestellen")
                exit()
        else:
            print("sorry geen idee wat je bedoel, hier een glaasje")