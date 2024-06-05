def name_age():
    dict = {}
    dict['name'] = input("wat is je naam?: ")
    dict['age'] = input("hoe oud ben je?: ")
    return dict
    


totaal = name_age()
print(f"{totaal['name']} is {totaal['age']} jaar")