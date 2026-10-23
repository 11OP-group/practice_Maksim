all_even = True

for _ in range(10):
    number = int(input())
    if number % 2 != 0:
        all_even = False

if all_even:
    print("YES")
else:
    print("NO")