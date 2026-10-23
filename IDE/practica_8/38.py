n = int(input())
total_sum = 0

for i in range(1, n + 1):
    total_sum += ((-1) ** (i + 1)) * i

print(total_sum)