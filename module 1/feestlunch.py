from termcolor import colored
start = str(input("mot je wat hebben?: ")).lower()
PRIJS_CROISANT = 0.39
PRIJS_STOKBROOD = 2.78
COUPON_KORTING = 0.50


print(colored("menukaart:", "red"))
print(colored("croissant €0,39", "yellow"))
print(colored("stokbrood €2,78", "yellow"))

aantal_croisant = int(input("hoeveel croissants moet je?: "))
aantal_stokbrood = int(input("hoeveel stokbrood moet je?: "))

prijs_croisant_stokbrood = (aantal_croisant * PRIJS_CROISANT) + (aantal_stokbrood * PRIJS_STOKBROOD)

print(colored(f"dat is €{prijs_croisant_stokbrood}", "green"))

vraag_coupon = str(input("heb je nog coupons?: ")).lower()
if vraag_coupon == "yes":
    aantal_coupons = int(input("hoeveel heb je er?: "))
    prijs_croisant_stokbrood = prijs_croisant_stokbrood - (aantal_coupons * COUPON_KORTING)
    print(colored(f"dan is het €{prijs_croisant_stokbrood}", "green"))
elif vraag_coupon == "no":
    print(colored("tot ziens", "green"))