gastheer = str(input("wie is de gastheer?: "))
gasten = 21
drank = True
chips = False

if (chips == True and drank == True and gasten == True) and (gastheer != "" and gastheer != "Corbijn" and drank == True) and (gasten >= 4 and gasten <= 20):
    print('Start the Party')
else:
    print('No Party')