BANKNOTES = [5000, 2000, 1000, 500, 200, 100]

def calculate_withdrawal(amount):
    result = {}
    remaining = amount
    for nominal in BANKNOTES:
        count = remaining // nominal
        if count > 0:
            result[nominal] = count
            remaining -= count * nominal
    return result

amount = int(input("Введите сумму для снятия (кратна 100): "))

if amount % 100 != 0 or amount <= 0:
    print("Ошибка: сумма должна быть положительной и кратна 100.")
else:
    print(f"Запрошена сумма: {amount:,} руб.")
    withdrawal = calculate_withdrawal(amount)
    for nominal in BANKNOTES:
        count = withdrawal.get(nominal, 0)
        if count:
            print(f"Купюр по {nominal:>5} руб.: {count} шт.")
    total = sum(n * c for n, c in withdrawal.items())
    print(f"Итого выдано: {total:,} руб.")
