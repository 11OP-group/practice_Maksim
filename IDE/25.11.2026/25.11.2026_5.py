print('введите числа через пробел')
numbers=[int(item) for item in input().split()]

pairs_count= 0
list_length=len(numbers)

for i in range(list_length):
    for j in range(i+ 1, list_length):
        if numbers[i]==numbers[j]:
            pairs_count+=1
print(f'колличество пар элементов равных друг другу{pairs_count}')