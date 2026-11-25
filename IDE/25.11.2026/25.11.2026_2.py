line=int(input('введите количество строк'))
all_chars=[]

for _ in range(line):
    num=(input('введите число'))
    all_chars.extend(num)

print(f'всех введёных чисел{all_chars}')