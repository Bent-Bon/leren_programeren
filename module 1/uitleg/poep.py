artiesten = ['DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH', 'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH', 'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA', 'DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH', 'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH', 'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA',"kayzo"]
artiesten_telling = {}

for artiest in artiesten:
    if artiest in artiesten_telling:
        artiesten_telling[artiest] += 1
    else:
        artiesten_telling[artiest] = 1


for artiest, telling in artiesten_telling.items():
    print(f"{artiest}: {telling} keer")
