def convertToEuroText (amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

SMALL_PRICE_2 = 1.25
MEDIUM_PRICE_2 = 2.10

amount_s = float(input('Hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(SMALL_PRICE))))
amount_m = float(input('En hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(MEDIUM_PRICE))))
totalPrice = float(amount_s * SMALL_PRICE_2) + float(amount_m * MEDIUM_PRICE_2)

print('Dat is dan {} totaal'.format(convertToEuroText(totalPrice)))