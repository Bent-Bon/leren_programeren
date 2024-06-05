def fibonacci(number1, number2, length):
    list = [number1, number2]
    for x in range(length):
        number3 = (number1 + number2)
        list.append(number3)
        number1 = number2
        number2 = number3
    return list
print(fibonacci(7, 5, 7))