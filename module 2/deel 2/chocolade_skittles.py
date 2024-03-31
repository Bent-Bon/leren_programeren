import random
colors = ["red", "blue", "green", "yellow", "brown"]
zak = []
new_dict = {}
number = int(input("hoeveel chocolade skittles moeten er in de zak?: "))

for x in range(number):
    random_kleur = (random.choice(colors))
    # stap 1: voeg toe aan zak
    zak.append(random_kleur)
    #stap 2:houd telling bij in dict
    if random_kleur in new_dict:
        new_dict[random_kleur] += 1
    else:
        new_dict[random_kleur] = 1

print(zak)



# for color in colors:
    
#     count = zak.count(color)
#     new_dict[colors] = count
for x, y in new_dict.items():
    print(x, y)




# artiesten = ['DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH', 'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH', 'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA', 'DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH', 'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH', 'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA',"kayzo"]
# artiesten_telling = {}

# for artiest in artiesten:
#     if artiest in artiesten_telling:
#         artiesten_telling[artiest] += 1
#     else:
#         artiesten_telling[artiest] = 1


# for artiest, telling in artiesten_telling.items():
#     print(f"{artiest}: {telling} keer")