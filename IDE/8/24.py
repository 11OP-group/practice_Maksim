def file_manager():
    print("📂 Менеджер файлов")
    print("-" * 40)

    while True:
        print("\nВыберите действие:")
        print("1. Создать новый файл")
        print("2. Записать текст в файл")
        print("3. Прочитать файл")
        print("4. Удалить файл")
        print("5. Выйти")

        choice = input("Ваш выбор: ")

        match choice:
            case '1':
                filename = input("Введите имя файла: ")
                try:
                    with open(filename, 'x') as file:
                        print(f"✅ Файл '{filename}' успешно создан")
                except FileExistsError:
                    print("⚠️ Файл уже существует!")

            case '2':
                filename = input("Введите имя файла: ")
                text = input("Введите текст для записи: ")
                try:
                    with open(filename, 'a') as file:
                        file.write(text + '\n')
                        print("✅ Текст успешно записан")
                except FileNotFoundError:
                    print("⚠️ Файл не найден!")

            case '3':
                filename = input("Введите имя файла: ")
                try:
                    with open(filename, 'r') as file:
                        content = file.read()
                        print("\n📄 Содержимое файла:")
                        print("-" * 40)
                        print(content)
                        print("-" * 40)
                except FileNotFoundError:
                    print("⚠️ Файл не найден!")

            case '4':
                filename = input("Введите имя файла для удаления: ")
                try:
                    import os
                    os.remove(filename)
                    print(f"✅ Файл '{filename}' успешно удален")
                except FileNotFoundError:
                    print("⚠️ Файл не найден!")

            case '5':
                print("👋 До свидания!")
                break

            case _:
                print("❌ Неверный выбор. Попробуйте снова.")


# Запуск программы
file_manager()
