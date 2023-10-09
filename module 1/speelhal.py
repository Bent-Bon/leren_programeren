from termcolor import colored
start = str(input("spelen?: ")).lower()
sand = 7.45
geld_verlies = 0.37


if start == "yes":
    print(colored("menukaart:", "red"))
    print(colored("dagkaart €7.45", "yellow"))

    cro = int(input("hoeveel tickets wil je?: "))

    isk = (cro * sand)

    print(colored(f"dat is €{isk}", "green"))

    oculus = str(input("wil je de VIP-VR-GameSeat gebruiken?: ")).lower()
    if oculus == "yes":
        coupon = int(input("hoeveel minuten wil je? (gaat per 5 minuten): "))
        isk = isk + (coupon * geld_verlies)
        if cro == 4 and coupon == 45:
            print("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro")
        else:
            print(colored(f"dan is het €{isk}", "green"))
    elif oculus == "no":
        print(colored("tot ziens", "green"))
elif start == "no":
    print(colored("dat is spijtig", "red"))
else:
    print(colored("wut?", "red"))