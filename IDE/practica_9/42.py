num = int(input())

operating_num = 1

while operating_num <= num:
    if 5 <= operating_num <= 9:
        operating_num += 1
        continue
    if 17 <= operating_num <= 37:
        operating_num += 1
        continue
    if 78 <= operating_num <= 87:
        operating_num += 1
        continue

    print(operating_num)

    operating_num += 1