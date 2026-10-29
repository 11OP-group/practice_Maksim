price = int(input())

coins_total = 0

while price > 0:
    if price >= 25:
        coins_total += price // 25
        price %= 25
    elif price >= 10:
        coins_total += price // 10
        price %= 10
    elif price >= 5:
        coins_total += price // 5
        price %= 5
    else:
        coins_total += price  # Оставшиеся монеты номиналом 1
        price = 0

print(f"{coins_total}")
