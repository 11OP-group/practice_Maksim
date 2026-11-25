import random

marks=[random.randint(2,5) for _ in range(10)]
print(f'список оцепнок:{marks}')

fives_count=0
twos_count=0

for mark in marks:

    if mark == 5:
        fives_count+=1

    elif mark == 2:
        twos_count+=1

print(f'колличество пятёрок:{fives_count}')
print(f'колличество двоек:{twos_count}')