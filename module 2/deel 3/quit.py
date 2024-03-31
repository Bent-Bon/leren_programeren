counter = 0

while True:
    vraag = input("?").lower()
    if vraag == "quit":
        print(f"je bent {counter} keer `?` gevraagd")
        break
    # else:
    counter += 1