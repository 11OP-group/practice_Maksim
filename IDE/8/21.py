def currency_converter():
    # Курсы валют (примерные значения)
    exchange_rates = {
        'USD': 1.0,  # Базовый курс
        'EUR': 0.92,  # Евро
        'RUB': 95.5,  # Российский рубль
        'GBP': 0.82,  # Британский фунт
        'JPY': 147.5  # Японская иена
    }

    print("💵 Конвертер валют")
    print("Доступные валюты:")
    for currency in exchange_rates:
        print(f"- {currency}")

    while True:
        # Выбор исходной валюты
        from_currency = input("\nВведите исходную валюту (например, USD): ").upper()
        if from_currency not in exchange_rates:
            print("⚠️ Неверная валюта. Попробуйте снова.")
            continue

        # Выбор целевой валюты
        to_currency = input("Введите целевую валюту: ").upper()
        if to_currency not in exchange_rates:
            print("⚠️ Неверная валюта. Попробуйте снова.")
            continue

        try:
            # Ввод суммы
            amount = float(input(f"\nВведите сумму в {from_currency}: "))
            if amount < 0:
                print("⚠️ Сумма не может быть отрицательной")
                continue

            # Расчет конвертации
            rate_from = exchange_rates[from_currency]
            rate_to = exchange_rates[to_currency]

            converted_amount = (amount / rate_from) * rate_to

            # Вывод результата
            print(f"\n💹 Результат конвертации:")
            print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

        except ValueError:
            print("❌ Ошибка: введите числовое значение суммы")

        # Повтор конвертации
        repeat = input("\nХотите конвертировать еще? (да/нет): ").lower()
        if repeat != 'да':
            print("👋 До свидания!")
            break


# Запуск программы
currency_converter()
