def name_age():
    dict = {}
    dict['name'] = input("wat is je naam?: ")
    dict['age'] = input("hoe oud ben je?: ")
    dict['city'] = input("in welke stad woon je?: ")
    return dict

def meerdere():
    dict_lijst = []
    while True:
        totaal = name_age()
        dict_lijst.append(totaal)
        if input("Toets enter om door te gaan of stop om te printen: ").lower() == "stop":
            return dict_lijst
            break