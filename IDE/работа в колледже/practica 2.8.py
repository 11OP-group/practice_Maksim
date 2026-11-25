import random

random_num =[random.randint(1,100) for _ in range(5)]

min_value = min(random_num)
min_index = 0

for i in range(len(random_num)):
    if random_num[i] == min_value:
        min_index= i
        break

random_num[0], random_num[min_index]=random_num[min_index],random_num[0]

print(random_num)