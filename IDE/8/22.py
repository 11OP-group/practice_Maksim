def grade_system():
    grades = []

    print("🎓 Система учета успеваемости")
    while True:
        print("\nВыберите действие:")
        print("1. Добавить оценку")
        print("2. Посмотреть средний балл")
        print("3. Вывести все оценки")
        print("4. Выход")

        choice = input("Ваш выбор: ")

        match choice:
            case '1':
                try:
                    grade = float(input("Введите оценку (0-10): "))
                    if 0 <= grade <= 10:
                        grades.append(grade)
                        print("✅ Оценка добавлена")
                    else:
                        print("⚠️ Неверный диапазон оценки")
                except ValueError:
                    print("❌ Введите число")

            case '2':
                if grades:
                    average = sum(grades) / len(grades)
                    print(f"Средний балл: {average:.2f}")
                else:
                    print("📚 Нет оценок для подсчета")

            case '3':
                if grades:
                    print("📋 Ваши оценки:")
                    for i, grade in enumerate(grades, 1):
                        print(f"{i}. {grade}")
                else:
                    print("📚 Нет оценок")

            case '4':
                print("👋 До свидания!")
                break

            case _:
                print("❌ Неверный выбор")


grade_system()
