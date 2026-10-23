num = int(input())

max1 = -1
max2 = -1

for _ in range(num):
    current_num = int(input())

    if current_num > max1:
        max2 = max1
        max1 = current_num
    elif current_num > max2:
        max2 = current_num

print(max1)
print(max2)