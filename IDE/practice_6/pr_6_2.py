MIN_POCKET = 0
MAX_POCKET = 36

pocket = int(input("Введите номер кармана (0–36): "))

if not MIN_POCKET <= pocket <= MAX_POCKET:
    print("ошибка ввода")
elif pocket == 0:
    print("зелёный")
elif 1 <= pocket <= 10 or 19 <= pocket <= 28:
    print("красный" if pocket % 2 != 0 else "чёрный")
elif 11 <= pocket <= 18 or 29 <= pocket <= 36:
    print("чёрный" if pocket % 2 != 0 else "красный")
