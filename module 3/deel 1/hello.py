def hallo(number:int):
    zin = ""
    for x in range(number):
        zin += f"Hello from function town {x + 1}!\n"
    return zin
print(hallo(7))