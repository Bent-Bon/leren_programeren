# gemiddled aantal extra woorden per zin
# zin eindigd ook op iets anders dan een punt

line = input("Enter Input: ").split()
count = []
vertaling = {
    "de": "het",
    "druk": "rust",
    "of": "en",
    "een": "twee",
    "muis": "rat"
}
zinnen = {}
zin_tel = 0

for woord in line:
    print(woord)
    if woord in vertaling:
        line.append(vertaling[woord])
    else:
        line.append(woord)
    count.append(len(woord))
line = ' '.join(line)
print(line)
print(count)


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