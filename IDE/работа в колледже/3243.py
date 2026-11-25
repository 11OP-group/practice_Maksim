attempts=3

while attempts > 0:
    password=input("введите пароль:")

    if password == "admin":
        print("Доступ разрешён")
        break

    attempts -=1
    print("Доступ запрещён")
