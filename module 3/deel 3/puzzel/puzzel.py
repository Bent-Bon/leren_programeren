reeks = str(input("Wat is het eerste getal?: "))
nieuwe_reeks = ""
herkenner = ""
counter = 0
teller = 0

while True:
    for x in reeks:
        if x != herkenner:
            if herkenner:
                nieuwe_reeks += f"{counter}{herkenner}"
            herkenner = x
            counter = 1
        else:
            counter += 1

    if herkenner:
        nieuwe_reeks += f"{counter}{herkenner}"
    
    print(nieuwe_reeks)

    reeks = nieuwe_reeks
    nieuwe_reeks = ""
    herkenner = ""
    counter = 0

    teller = 0
    for x in reeks:
        if x == '3':
            teller += 1
            if teller == 2:
                exit()
        else:
            teller = 0
