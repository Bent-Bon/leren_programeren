from termcolor import colored
prijs_dag = 7.45
prijs_vip = 0.074



print(colored("dagkaart €7.45", "yellow"))

aantal_dagkaart = int(input("hoeveel tickets wil je?: "))

kosten_dagkaart = (aantal_dagkaart * prijs_dag)
kosten_dagkaart = round(kosten_dagkaart, 2)

print(colored(f"dat is €{kosten_dagkaart}", "green"))

vraag_vip = str(input("wil je de VIP-VR-GameSeat gebruiken?: ")).lower()
if vraag_vip == "yes":
    print(colored("5 minuten vip kost €0.37", "yellow"))
    aantal_vip = int(input("hoeveel minuten wil je?: "))
    kosten_dagkaart = kosten_dagkaart + (aantal_vip * prijs_vip)
    kosten_dagkaart = round(kosten_dagkaart, 2)
    print(colored(f"dan wordt dan €{kosten_dagkaart}", "green"))
    
elif vraag_vip == "no":
    print(colored("tot ziens", "green"))