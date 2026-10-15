import random
import string


def password_generator():
    print("🔐 Генератор паролей")
    length = int(input("Длина пароля (минимум 8 символов): "))

    if length < 8:
        print("⚠️ Пароль слишком короткий!")
        return

    has_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
    has_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
    has_special = input("Использовать спецсимволы? (y/n): ").lower() == 'y'

    all_chars = string.ascii_lowercase
    if has_uppercase:
        all_chars += string.ascii_uppercase
    if has_digits:
        all_chars += string.digits
    if has_special:
        all_chars += string.punctuation

    if not all_chars:
        print("⚠️ Выберите хотя бы один тип символов")
        return

    password = ''.join(random.choice(all_chars) for _ in range(length))
    print(f"\n🔑 Сгенерированный пароль: {password}")


password_generator()
