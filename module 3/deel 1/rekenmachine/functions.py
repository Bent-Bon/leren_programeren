def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2

def number():
    while True:
        number = input("wat is je getal?: ")
        try:
            number = float(number)
            if number.is_integer():
                return int(number)
            else:
                return number
        except ValueError:
            print("The input must be a number (int or float).")