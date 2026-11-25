sum=0

while True:

    price=int(input())
    if price==0:
        break
    if price<0:
        print("Ошибка цены")
        continue
    sum+=price

if sum>1000:
    final_sum=sum*0.9
    print("итоговая сумма с учётом скидки",final_sum)
else:
    print("итоговая сумма")