m = float(input())
p = float(input())
n = int(input())

population = m

for day in range(1, n + 1):
    if day > 1:
        population += population * (p / 100)

    print(f"{day} {population}")