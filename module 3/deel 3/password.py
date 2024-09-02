import random
hoofdletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
speciale_characters = ["@", "#", "$", "%", "_", "?"]
nummers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
hoofdletter_hoeveelheid = random.randint(2, 6)
letter_hoeveelheid = "?"
speciale_character_hoeveelheid = 3
nummer_hoeveelheid = random.randint(4, 7)
max_hoeveelheid = 24
letter_hoeveelheid = max_hoeveelheid - (hoofdletter_hoeveelheid + speciale_character_hoeveelheid + nummer_hoeveelheid)
wachtwoord = []

for x in range(letter_hoeveelheid):
    letter = random.choice(letters)
    wachtwoord.append(letter)

for x in range(speciale_character_hoeveelheid):
    speciale_character = random.choice(speciale_characters)
    wachtwoord.append(speciale_character)

for x in range(nummer_hoeveelheid):
    nummer = random.choice(nummers)
    wachtwoord.append(nummer)

for x in range(hoofdletter_hoeveelheid):
    hoofdletter = random.choice(hoofdletters)
    wachtwoord.append(hoofdletter)

print(''.join(wachtwoord))