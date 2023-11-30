cijfer_lijst = []

jaar = int(input("hoeveel weken zit je op school?: "))

print("hoevaak ben je gestrest?: ")
while True:
    vraag_1 = int(input("0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit: "))
    if vraag_1 == 0:
        break
    elif vraag_1 in (1,2,3,4):
            cijfer_lijst.append(vraag_1)
            break
    else:
        print('Probeer opnieuw.')

print("hoevaak ben je gestrest?: ")
while True:
    vraag_2 = int(input("0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit: "))
    if vraag_2 == 0:
        break
    elif vraag_2 in (1,2,3,4):
            cijfer_lijst.append(vraag_2)
            break
    else:
        print('Probeer opnieuw.')


print("hoevaak kom je te laat?: ")
while True:
    vraag_3 = int(input("0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit: "))
    if vraag_3 == 0:
        break
    elif vraag_3 in (1,2,3,4):
            cijfer_lijst.append(vraag_3)
            break
    else:
        print('Probeer opnieuw.')

print("hoevaak heb je je werk af?: ")
while True:
    vraag_4 = int(input("0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit: "))
    if vraag_4 == 0:
        break
    elif vraag_4 in (1,2,3,4):
            cijfer_lijst.append(vraag_4)
            break
    else:
        print('Probeer opnieuw.')

print("hoevaak vergeet je je spullen?: ")
while True:
    vraag_5 = int(input("0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit: "))
    if vraag_5 == 0:
        break
    elif vraag_5 in (1,2,3,4):
            cijfer_lijst.append(vraag_5)
            break
    else:
        print('Probeer opnieuw.')

if jaar >= 10:

    print("hoevaak wil je niet komen?: ")
    while True:
        vraag_6 = int(input("0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit: "))
        if vraag_6 == 0:
            break
        elif vraag_6 in (1,2,3,4):
            cijfer_lijst.append(vraag_6)
            break
        else:
            print('Probeer opnieuw.')

    print("ga je oprijd slapen?: ")
    while True:
        vraag_7 = int(input("0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit: "))
        if vraag_7 == 0:
            break
        elif vraag_7 in (1,2,3,4):
            cijfer_lijst.append(vraag_7)
            break
        else:
            print('Probeer opnieuw.')

    all_score = sum(cijfer_lijst)
    if all_score <= 5:
        print("zorgelijk advies")
    elif all_score <= 28:
        print("twijfelachtig advies")
    else:
        print("gerust advies")

else:
    pass
if jaar < 10:
    all_score = sum(cijfer_lijst)
    if all_score <= 3:
        print("zorgelijk advies")
    elif all_score <= 20:
        print("twijfelachtig advies")
    else:
        print("gerust advies")
else:
    pass

