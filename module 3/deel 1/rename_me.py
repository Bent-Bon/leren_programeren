def even_or_odd(checker:int) -> bool:
    return checker % 2 == 0

def zin_reverser(input_zin:str) -> str:
    splitt_zin = input_zin.split()
    reversed_splitt_zin = splitt_zin[::-1]
    zin_complete_revered = ' '.join(reversed_splitt_zin)
    return zin_complete_revered

def character_counter(input_str:str) -> int:
    all_char = set(input_str)
    count_all_char = len(all_char)
    return count_all_char

def gemidelde_aantal_letters(input_str:str) -> float:
    str_split = input_str.split()
    
    counter = 0
    for woord in str_split:
        counter += len(woord)

    gemideld = counter / len(str_split)
    return gemideld

def hele_tafel(teller:int, noemer:int=10) -> None:
    for keer_getal in range(1, noemer+1):
        andwoord = keer_getal * teller
        print(f'{keer_getal} x {teller} = {andwoord}')

print(hele_tafel(10))