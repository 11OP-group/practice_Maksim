number = int(input())

last_digit = number % 10

count_threes = 0
count_last_digit = 0
count_evens = 0
sum_greater_five = 0
product_greater_seven = 1
count_zeros_and_fives = 0

temp_number = number

# Цикл разбирает число с конца, пока оно не станет равным 0
while temp_number > 0:
    digit = temp_number % 10

    # 1. Количество цифр 3
    if digit == 3:
        count_threes += 1

    # 2. Сколько раз встречается последняя цифра
    if digit == last_digit:
        count_last_digit += 1

    # 3. Количество чётных цифр
    if digit % 2 == 0:
        count_evens += 1

    # 4. Сумма цифр, больших 5
    if digit > 5:
        sum_greater_five += digit

    # 5. Произведение цифр, больших 7
    if digit > 7:
        product_greater_seven *= digit

    # 6. Сколько раз встречаются цифры 0 и 5 суммарно
    if digit == 0 or digit == 5:
        count_zeros_and_fives += 1

    temp_number //= 10

print(f"{count_threes}")
print(f"{count_last_digit}")
print(f"{count_evens}")
print(f"{sum_greater_five}")
print(f"{product_greater_seven}")
print(f"{count_zeros_and_fives}")
