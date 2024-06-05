from functions import *

def calculator():
    func_checker_eerste_helft = ["a", "b", "c", "d", ""]
    func_checker_tweede_helft = ["e", "f", "g", "h"]
    number1 = input("wat is je eerste nummer?: ")
    tekst = "wat wilt u doen?"
    full_som = ""
    while True:
        while True:
            func = input(f"{tekst} \n getallen optellen, A) \n getallen aftrekken, B) \n getallen vermenigvuldigen, C) \n getallen delen, D) \n getal ophogen, E) \n getal verlagen, F) \n getal verdubbelen, G) \n getal halveren?, H) \n of niets om te stoppen").lower()
            if func not in func_checker_eerste_helft or func not in func_checker_tweede_helft:
                print("ongeldige invoer")
            elif func in func_checker_eerste_helft:
                if func == "":
                    exit()
                number2 = input("wat is je tweede nummer?: ")
                break
            elif func in func_checker_tweede_helft:
                if func == "e" or func == "f":
                    number2 = 1
                else:
                    number2 = 2
                break


        if func == "a":
            andwoord = addition(number1, number2)
            opperator = "+"
        elif func == "b":
            andwoord = subtraction(number1, number2)
            opperator = "-"
        elif func == "c":
            andwoord = multiplication(number1, number2)
            opperator = "*"
        elif func == "d":
            andwoord = division(number1, number2)
            opperator = "/"
        elif func == "e":
            andwoord = addition(number1, number2)
            opperator = "+"
        elif func == "f":
            andwoord = subtraction(number1, number2)
            opperator = "-"
        elif func == "g":
            andwoord = subtraction(number1, number2)
            opperator = "*"
        elif func == "h":
            andwoord = subtraction(number1, number2)
            opperator = "/"
        full_som += f"{number1} {opperator} {number2} = {andwoord} \n"
        tekst = f"{full_som} Wil je wat met de uitkomst?"
        number1 = andwoord

calculator()