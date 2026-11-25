from sys import prefix

number = int(input("Введите число"))



if number == 0:
    print("Зеленое")
else:
    if number <= 36:
        if 1 <= number <= 10 or 19 <= number <= 28:
            if number %2 != 0:
                print("красный")
            else:
                print("черный")
        elif 11 <= number <= 18 or 29 <= number <= 36:
            if number %2 != 0:
                print("черный")
            else:
                print("красный")
    else:
        print("Пределелы")