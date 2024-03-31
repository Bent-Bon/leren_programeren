def generate_lists():
    num_lists = int(input("Hoeveel lijstjes? "))
    lists = []

    for i in range(1, num_lists + 1):
        list_length = int(input(f"Hoeveel in lijst {i}? "))
        # new_list = [j * i for j in range(1, list_length + 1)] #korte versie
        new_list = []
        for j in range(1, list_length + 1):
            new_list.append(j * i)
        lists.append(new_list)

    return lists

result = generate_lists()
print(result)