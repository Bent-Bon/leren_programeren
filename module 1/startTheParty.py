gastheer = str(input("wie is de gastheer?: "))
gasten = int(input("hoeveel gasten zijn er?: "))
drank = True
chips = False

if (chips or drank and gasten > 0 and gasten < 20) and (gastheer != "" and gastheer != "Corbijn" and drank) or (gastheer == "bent"):
    print('Start the Party')
else:
    print('No Party')