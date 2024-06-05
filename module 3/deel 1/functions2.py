def name_age():
    namen_str = ""
    namen_str2 = ""
    dict_lijst = []
    while True:
        name = input("wat is je naam?: ")
        age = input("hoe oud ben je?: ")
        city = input("in welke stad woon je?: ")
        dict_lijst.append({"name" : name, "age" : age, "city" : city})
        if input("Toets enter om door te gaan of stop om te printen: ").lower() == "stop":
            break

    for person in dict_lijst:
        namen_str += f"{person['name']}, die in {person['city']} woont, is {person['age']} jaar \n"
        namen_str2 += f"in {person['city']} woont de {person['age']} jarige {person['name']}\n"
    return namen_str, namen_str2