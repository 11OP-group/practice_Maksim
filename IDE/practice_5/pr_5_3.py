USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    return amount_usd * USD_TO_RUB

amount = float(input("Введите сумму в долларах: "))
result = convert_usd_to_rub(amount)

print(f"{amount:.2f} $ = {result:,.2f} руб. (курс {USD_TO_RUB})")
