def dukaten(bedragen):
    return round(bedragen * 100 / 5) * 5 / 100

print(dukaten(2.23))
print(dukaten(2.22))
print(dukaten(2.27))
print(dukaten(2.28))
print(dukaten(2.25))