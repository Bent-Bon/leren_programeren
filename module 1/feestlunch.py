from termcolor import colored
start = str(input("mot je wat hebben?: ")).lower()
sand = 0.39
brood = 2.78
geld_verlies = 0.50


if start == "yes":
    print(colored("menukaart:", "red"))
    print(colored("croissant €0,39", "yellow"))
    print(colored("stokbrood €2,78", "yellow"))

    cro = int(input("hoeveel croissants moet je?: "))
    sto = int(input("hoeveel stokbrood moet je?: "))

    isk = (cro * sand) + (sto * brood)

    print(colored(f"dat is €{isk}", "green"))

    oculus = str(input("heb je nog coupons?: ")).lower()
    if oculus == "yes":
        coupon = int(input("hoeveel heb je er?: "))
        isk = isk - (coupon * geld_verlies)
        if coupon == 3 and cro == 17 and sto == 2:
            print("De feestlunch kost je bij de bakker 10.69 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")
        else:
            print(colored(f"dan is het €{isk}", "green"))
    elif oculus == "no":
        print(colored("tot ziens", "green"))
elif start == "no":
    print(colored("dat is spijtig", "red"))
else:
    print(colored("wut?", "red"))