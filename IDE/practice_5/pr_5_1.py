TAX = 0.13

annual = float(input("Введите ваш годовой доход: "))

tax = annual * TAX
net = annual - tax

print(f"Общая сумма дохода:    {annual:>14,.2f} руб.")
print(f"Сумма налога (13%):   {tax:>14,.2f} руб.")
print(f"Сумма «на руки»:      {net:>14,.2f} руб.")
