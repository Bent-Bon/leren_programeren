#Bent Bon
L_PIZZA = 13.99
M_PIZZA = 9.99
S_PIZZA = 7.99
BTW_PERCENTAGE = 9


print("hallo wij hebben een asortiment van")
print(f"(45 cm) grote pizza's €{L_PIZZA}")
print(f"(30 cm) middel pizza's €{M_PIZZA}")
print(f"(20 cm) kleine pizza's €{S_PIZZA}")

groote_pizza = int(input("hoeveel grote pizza's wil je?: "))
prijs_L_pizza = groote_pizza * L_PIZZA

middel_pizza = int(input("hoeveel middel pizza's wil je?: "))
prijs_M_pizza = (middel_pizza * M_PIZZA)

kleine_pizza = int(input("hoeveel kleine pizza's wil je?: "))
prijs_S_pizza = kleine_pizza * S_PIZZA

totaal = prijs_L_pizza + prijs_M_pizza + prijs_S_pizza
btw = totaal / 100 * BTW_PERCENTAGE
btw_totaal = totaal + btw

print(f"aantal groote pizza('s) {groote_pizza} €{prijs_L_pizza}")
print(f"aantal middel pizza('s) {middel_pizza} €{prijs_M_pizza}")
print(f"aantal kleine pizza('s) {kleine_pizza} €{prijs_S_pizza}")
print(f"totaal €{totaal}")
print(f"btw €{btw}")
print(f"totaal met btw €{btw_totaal}")