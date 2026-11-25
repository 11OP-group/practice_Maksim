numbers = [ 10,20,30,40,50]
num=int(input())

found= False

for i in range(len(numbers)):
    if numbers[i] == num:
        print(f'число {num} под индексом {i}')
        found=True
        break

if not found:
    print('нет такого числа')