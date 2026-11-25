print("Введите три число по очереди")
num1 = int(input("Первое число:"))

while True:
    num2 = int(input("Второе число:"))
    if num1>=num2:
        print("Ошибка введите второе число заново")
        continue
    else:
        break

while True:
    num3=int(input("Третье число:"))
    if num2>=num3:
        print("Ошибка введите третье число заново")
        continue
    else:
        print("Последовательность принята")
        break