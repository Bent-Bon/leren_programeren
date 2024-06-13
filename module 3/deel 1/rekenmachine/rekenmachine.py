from functions import *

func_checker_extra_opp = ["e", "f", "g", "h"]
func_checker = ["a", "b", "c", "d", "e", "f", "g", "h", ""]
tekst = "wat wilt u doen?"
full_som = ""
firstround = True
while True:
    while True:
        func = input(f"{tekst} \n getallen optellen, A) \n getallen aftrekken, B) \n getallen vermenigvuldigen, C) \n getallen delen, D) \n getal ophogen, E) \n getal verlagen, F) \n getal verdubbelen, G) \n getal halveren?, H) \n of niets om te stoppen: ").lower()
        if func not in func_checker:
            print("ongeldige invoer")
        else:
            if func == "":
                if firstround == False:
                    exit()
                else:
                    print("u heeft nog niets ingevoerd")
            while True:
                if firstround == True:
                    print("eerste nummer")
                    number1 = number()
                firstround = False
                if func not in func_checker_extra_opp:
                    print("tweede nummer")
                    number2 = number()
                if func == "d" and number2 == 0:
                    print("u kan niet delen door 0")
                else:
                    break
            break

    if func == "a":
        andwoord = addition(number1, number2)
        opperator = "+"
        opperator_str = "optellen"

    elif func == "b":
        andwoord = subtraction(number1, number2)
        opperator = "-"
        opperator_str = "aftrekken"

    elif func == "c":
        andwoord = multiplication(number1, number2)
        opperator = "*"
        opperator_str = "vermenigvuldigen"

    elif func == "d":
        andwoord = division(number1, number2)
        opperator = "/"
        opperator_str = "delen"

    elif func == "e":
        andwoord = addition(number1, 1)
        opperator = "+"
        opperator_str = "ophogen"

    elif func == "f":
        andwoord = subtraction(number1, 1)
        opperator = "-"
        opperator_str = "verlagen"

    elif func == "g":
        andwoord = multiplication(number1, 2)
        opperator = "*"
        opperator_str = "verdubbelen"

    elif func == "h":
        andwoord = division(number1, 2)
        opperator = "/"
        opperator_str = "halveren"
    
    if func in func_checker_extra_opp:
        if func == "h" or func == "g":
            full_som += f"{number1} {opperator} 2 = {andwoord} \n"
        else:
            full_som += f"{number1} {opperator} 1 = {andwoord}"
    else:
        full_som += f"{number1} {opperator} {number2} = {andwoord} \n"
    tekst = f"{opperator_str} \n {full_som} Wil je wat met de uitkomst?"
    number1 = andwoord