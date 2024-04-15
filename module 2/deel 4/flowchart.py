import random

gok_rondes_teller = 0
rondjes_teller = 0
goed_teller = 0
slecht_teller = 0
spel_einde = False

while True:
    random_num = random.randint(1, 1000)
    print(random_num)
    while True:
        gok_getal = int(input("doe een gok: "))
        abs_verschil = abs(random_num - gok_getal)


        if gok_getal == random_num:
            print("je hebt het goed geraden")
            goed_teller += 1
            break
        else:
            if gok_getal > random_num:
                higher_lower = "lager"
            else:
                higher_lower = "groter"
            print(f"je hebt het verkeerd geraden, het getal is {higher_lower}")
            print(f"het absolute verschil is: {abs_verschil}")
            if abs_verschil <= 20:
                print("Je bent heel warm")
            elif abs_verschil <= 50:
                print("Je bent warm")
            gok_rondes_teller += 1
            if gok_rondes_teller > 9:
                print("je hebt het niet goed geraden")
                print(f"het getal was: {random_num}")
                slecht_teller += 1
                break
            else:
                print(f"je zit nu in ronde: {gok_rondes_teller}")

    rondjes_teller += 1

    print(f"je hebt {rondjes_teller} rondes gespeeld")

    if rondjes_teller > 19:
        print("het spel eindigt hier")
        print("hier is je score")
        spel_einde = True
    
    print(f"je hebt {goed_teller} keer goed geraden")
    print(f"je hebt {slecht_teller} keer niet goed geraden")

    if spel_einde == True:
        break