def calculator():
    print("🔢 Калькулятор")
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Факториал")

    choice = input("Ваш выбор (1-5): ")

    match choice:
        case '1' | '2' | '3' | '4':
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            match choice:
                case '1':
                    result = num1 + num2
                    print(f"Результат: {num1} + {num2} = {result}")
                case '2':
                    result = num1 - num2
                    print(f"Результат: {num1} - {num2} = {result}")
                case '3':
                    result = num1 * num2
                    print(f"Результат: {num1} * {num2} = {result}")
                case '4':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"Результат: {num1} / {num2} = {result}")
                    else:
                        print("⚠️ Деление на ноль невозможно!")
        case '5':
            num = int(input("Введите число для вычисления факториала: "))
            if num < 0:
                print("⚠️ Факториал отрицательного числа не существует")
            else:
                result = 1
                for i in range(1, num + 1):
                    result *= i
                print(f"Результат: {num}! = {result}")
        case _:
            print("❌ Неверный выбор операции")


calculator()
