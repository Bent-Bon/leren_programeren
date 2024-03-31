am = 0
pm = -12
for x in range(24):
    am = am + 1
    pm = pm + 1
    if pm >= 1:
        print(f"{pm} pm")
    else:
        print(f"{am} am")