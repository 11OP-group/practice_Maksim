from datetime import datetime, timedelta


def date_calculator():
    print("📅 Калькулятор дат")
    print("-" * 40)

    while True:
        print("\nВыберите действие:")
        print("1. Рассчитать разницу между датами")
        print("2. Прибавить дни к дате")
        print("3. Отнять дни от даты")
        print("4. Текущая дата")
        print("5. Выйти")

        choice = input("Ваш выбор: ")

        match choice:
            case '1':
                try:
                    date1_str = input("Введите первую дату (YYYY-MM-DD): ")
                    date2_str = input("Введите вторую дату (YYYY-MM-DD): ")

                    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
                    date2 = datetime.strptime(date2_str, '%Y-%m-%d')

                    delta = date2 - date1
                    print(f"\n🔄 Разница между датами: {delta.days} дней")
                    print(f"или {delta.total_seconds()} секунд")

                except ValueError:
                    print("⚠️ Ошибка: неверный формат даты!")

            case '2':
                try:
                    date_str = input("Введите дату (YYYY-MM-DD): ")
                    days = int(input("Введите количество дней: "))

                    date = datetime.strptime(date_str, '%Y-%m-%d')
                    new_date = date + timedelta(days=days)
                    print(f"\n📅 Новая дата: {new_date.strftime('%Y-%m-%d')}")

                except ValueError:
                    print("⚠️ Ошибка: проверьте формат даты или количество дней!")

            case '3':
                try:
                    date_str = input("Введите дату (YYYY-MM-DD): ")
                    days = int(input("Введите количество дней: "))

                    date = datetime.strptime(date_str, '%Y-%m-%d')
                    new_date = date - timedelta(days=days)
                    print(f"\n📅 Новая дата: {new_date.strftime('%Y-%m-%d')}")

                except ValueError:
                    print("⚠️ Ошибка: проверьте формат даты или количество дней!")

            case '4':
                now = datetime.now()
                print(f"\n🕒 Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")

            case '5':
                print("👋 До свидания!")
                break

            case _:
                print("❌ Неверный выбор. Попробуйте снова.")


# Запуск программы
date_calculator()