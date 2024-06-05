from functions import *

lijst = meerdere()
for item in lijst:
    print(f"{item['name']}, die in {item['city']} woont, is {item['age']} jaar")