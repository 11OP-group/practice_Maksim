found_alexandra = False

people_count = 0

while True:
    name = input()

    if name == "Левон":
        break

    if found_alexandra:
        people_count += 1

    if name == "Александра":
        found_alexandra = True

print(f"{people_count}")
