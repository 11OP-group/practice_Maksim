print('введите числа через пробел')
numbers=[int(item) for item in input().split()]

numbers.sort()
pairs_count= 0

while len(numbers)>1:
    if numbers[0]==numbers[1]:
        pairs_count+=1
        numbers.pop(0)
        numbers.pop(0)
    else:
        numbers.pop(0)

print(f'колличество пар элементов равных друг другу{pairs_count}')