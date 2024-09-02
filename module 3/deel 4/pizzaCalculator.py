klanten_order = []
totaal = 0
teller = 0
pizza_prijzen = {
    "(45 cm) L_PIZZA": 13.99,
    "(30 cm) M_PIZZA": 9.99,
    "(20 cm) S_PIZZA": 7.99
}
BTW_PERCENTAGE = 9

print("Hallo, wij hebben een assortiment van:")
for pizza, prijs in pizza_prijzen.items():
    print(f"{pizza} €{prijs}")

for pizza, prijs in pizza_prijzen.items():
    try:
        hoeveelheid = int(input(f"Hoeveel {pizza}'s wil je?: "))
        if hoeveelheid < 0:
            print("Aantal kan niet negatief zijn.")
            continue
        klanten_order.append((pizza, hoeveelheid, prijs * hoeveelheid))
    except ValueError:
        print("Oeps, dat is geen geldig aantal.")

for pizza, hoeveelheid, prijs in klanten_order:
    print(f"Aantal {pizza}('s): {hoeveelheid} - Totaal: €{prijs:.2f}")

for _, _, prijs in klanten_order:
    totaal += prijs

btw = totaal / 100 * BTW_PERCENTAGE
totaal_met_btw = totaal + btw

print(f"Totaal: €{totaal:.2f}")
print(f"BTW ({BTW_PERCENTAGE}%): €{btw:.2f}")
print(f"Totaal met BTW: €{totaal_met_btw:.2f}")