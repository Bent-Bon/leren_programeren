import random
colors = ("orange", "blue", "green", "brown")
zak = []

number = int(input("hoeveel chocolade skittles moeten er in de zak?: "))

for x in range(number):
    zak.append(random.choice(colors))
print(zak)