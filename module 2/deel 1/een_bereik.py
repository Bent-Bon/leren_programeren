getal = int(input("Van welk getal wil je de tafel weten?"))
nummer = 0
for i in range(10):
    nummer =  nummer + 1
    formule = getal * nummer
    print(f"{getal} x {nummer} = {formule}")