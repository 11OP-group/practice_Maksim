prices_str='100,50,200,150,75,300'

prices_str=[int(x) for x in prices_str.split()]

max_price = max(prices_str)
prices_str.remove(max_price)

prices_str.append(max_price*0.5)

prices_str.sort()

print(", ".join(map(str, prices_str)))

average_price=sum(prices_str)/len(prices_str)
print(f'средняя цена:{average_price}')