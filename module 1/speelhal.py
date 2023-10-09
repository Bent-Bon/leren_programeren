from termcolor import colored
PRIJS_DAG = 7.45
PRIJS_VIP_5_MINUTEN =0.37
prijs_vip_minuut = PRIJS_VIP_5_MINUTEN / 5



print(colored(f"dagkaart €{PRIJS_DAG}", "yellow"))

aantal_dagkaart = int(input("hoeveel tickets wil je?: "))

kosten_dagkaart = (aantal_dagkaart * PRIJS_DAG)
kosten_dagkaart = round(kosten_dagkaart, 2)

print(colored(f"dat is €{kosten_dagkaart}", "green"))

vraag_vip = str(input("wil je de VIP-VR-GameSeat gebruiken?: ")).lower()
if vraag_vip == "yes":
    print(colored(f"5 minuten vip kost €{PRIJS_VIP_5_MINUTEN}", "yellow"))
    aantal_vip = int(input("hoeveel minuten wil je?: "))
    kosten_dagkaart = kosten_dagkaart + (aantal_vip * prijs_vip_minuut)
    kosten_dagkaart = round(kosten_dagkaart, 2)
    print(colored(f"dan wordt dan €{kosten_dagkaart}", "green"))
    
elif vraag_vip == "no":
    print(colored("tot ziens", "green"))