Home_balans=1000

print("Нажмите 1 чтобы узнать баланс")
print("Нажмите 2 чтобы снять 100 руб")
print("Нажмите 3 чтобы положить 100 руб")
print("Нажмите 4 чтобы выйти")

while True:

    num=int(input("Введите цифру"))
    if num==1:
        print(Home_balans)
        continue

    if num==2:
        if Home_balans>=100:
            Home_balans=Home_balans-100
            print("Снято баланс",Home_balans)
            continue
        else:
            print("недостаточно средств. Баланс",Home_balans)
            continue

    if num==3:
        Home_balans=Home_balans + 100
        print("баланс", Home_balans)
        continue

    if num==4:
        break