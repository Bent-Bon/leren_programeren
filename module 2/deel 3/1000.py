teller = 50
total = 0
# count = 0
som = str(teller)

while total < 1000:
    # count += 1
    teller += 1
    som += f" + {teller}"
    total += teller
    print(f"{teller - 50}: {som} = {total}")