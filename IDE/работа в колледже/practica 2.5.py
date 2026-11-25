data = [10,20,30,40,50,60,70,80,90,100]

firs_three=data[:3]
last_three=data[-3:]
reversed_data = data[::-1]
indices=data[1::2]

print(f'первая торйка чисел:{firs_three}')
print(f'последняя тройка чисел:{last_three}')
print(f'обртный порядок:{reversed_data}')
print(f'числа с нечётным индексом:{indices}')