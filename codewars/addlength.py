string = str(input("give scentence: "))
word_list = string.split()
count = []
full = []

for word in word_list:
    count.append(len(word))

for item in word_list:
    full.append(f"{item}: {count[word_list.index(item)]}")
print(full)
