# gemiddled aantal extra woorden per zin
# zin eindigd ook op iets anders dan een punt

line = input("geef een zin: ")
line_count = line
line = line.replace(".", "♚").replace("!", "♚").replace("?", "♚")
split_text = line.split("♚")

zinnen = {}
indeks = 0

for zin in split_text:
    aantal_woorden = len(zin.split())
    indeks += 1
    zinnen[f"zin {indeks}:"] = aantal_woorden
    if aantal_woorden <= 5:
        difficulty = "Excruciating"

    elif aantal_woorden <= 10:
        difficulty = "Formidable"

    elif aantal_woorden <= 15:
        difficulty = "Arduous"

    elif aantal_woorden <= 20:
        difficulty = "Strenuous"

    elif aantal_woorden > 20:
        difficulty = "Herculean"

    # print(f"Aantal woorden in zin {indeks}: {aantal_woorden}")
    print(f"Aantal woorden in zin {indeks}: {difficulty} ({aantal_woorden})")

print(zinnen)

# line = input("geef een zin: ")
# line = ("de het? of een. druk! muis")
# line_count = line
# vertaald = []
# vertaling = {
#     "de": "het",
#     "druk": "rust",
#     "of": "en",
#     "een": "twee",
#     "muis": "rat"
# }
# zinnen = {}
# indeks = 0

# split_text = line_count.replace(".", "♚").replace("!", "♚").replace("?", "♚").split("♚")
# print(split_text)


# for zin in split_text:
#     aantal_woorden = len(zin.split())
#     indeks += 1
#     zinnen.update({f"zin {indeks}:": {aantal_woorden}})
#     print(aantal_woorden)
#     print(zinnen)

# for woord in line:
#     if woord in vertaling:
#         vertaald.append(vertaling[woord])
#     else:
#         vertaald.append(woord)
#     zin_tel += 1



# vertaald = ' '.join(vertaald)
# print(vertaald)




# for letter in line:
#     if letter == ".":
#         zitten = True #kan weg
#         zin_tel += 1  
#         while zitten: #kan gwoon True
#             if line[zin_tel] != " ":
#                 line += line[zin_tel]
#                 zin_tel += 1
#             elif line[zin_tel] == " ":
#                 zitten = False #break
#         zinnen.update({zin_tel : line})

#         zin_tel += 1
#     else:
#         line += line[letter]

# average = sum(count)  / len(count)
# print("De gemiddelde lengte van een zin is", average, "letter.")



# if "." in line:
#     line = [line.split(".") for line in line]
#     print(line)
#     for palabra in line:
#         for x in count:
#             hele_zin = x + x
#             gemiddelde = int(hele_zin / len(count))
#         print(gemiddelde)
#         zinnen.update({zin_tel : gemiddelde})
#         zin_tel +=1
# else:
#     for x in count:
#         hele_zin = x + x
#         gemiddelde = int(hele_zin / len(count))
#     print(gemiddelde)
# print(zinnen)