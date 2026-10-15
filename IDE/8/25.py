def file_manager():
    print("📁 Менеджер файлов")
    while True:
        print("\nВыберите действие:")
        print("1. Создать файл")
        print("2. Записать в файл")
        print("3. Прочитать файл")
        print("4. Выход")

        choice = input("Ваш выбор: ")

        match choice:
            case '1':
                filename = input("Введите имя файла: ")
                try:
                    with open(filename, 'x') as file:
                        print(f"✅ Файл {filename} создан")
                except FileExistsError:
                    print("⚠️ Файл уже существует")

            case '2':
                filename = input("Введите имя файла: ")
                text = input("Введите текст для записи: ")
                try:
                    with open(filename, 'a') as file:
                        file.write(text + '\n')
                        print("✅ Текст записан")
                except FileNotFoundError:
                    print("⚠️ Файл не найден")

            case '3':
                filename = input("Введите имя файла: ")
                try:
                    with open(filename, 'r') as file:
                        content = file.read()
                        print(f"\n📄 Содержимое файла:\n{content}")
                except FileNotFoundError:
                    print("⚠️ Файл не найден")

            case '4':
                print("👋 До свидания!")
                break

            case _:
                print("❌ Неверный выбор")


file_manager()
