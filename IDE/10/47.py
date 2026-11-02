attempts = 3
while attempts > 0:
    password=input("введите пароль")

    if password == "admin":
        print('Доступ разрешен')
        break

    attempts -=1
    print("неверный пароль. Осталось попыток:",attempts)

if attempts == 0:
    print("Вход заблокирован")