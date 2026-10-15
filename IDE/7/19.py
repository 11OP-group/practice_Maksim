num1 = float(input())
op = input()
num2 = float(input())

match op:
    case '+':
        res = num1 + num2
        print(f"{num1} {op} {num2} = {res}")
    case '-':
        res = num1 - num2
        print(f"{num1} {op} {num2} = {res}")
    case '*':
        res = num1 * num2
        print(f"{num1} {op} {num2} = {res}")
    case '/':
        if num2 == 0:
            print("Ошибка: деление на ноль")
        else:
            res = num1 / num2
            print(f"{num1} {op} {num2} = {res}")
    case _:
        print("Неизвестная операция")