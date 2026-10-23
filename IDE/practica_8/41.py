import random

secret = random.randint(1, 10)
guessed = False

for attempt in range(1, 4):
    user_move = int(input("введите число от 1 до 10"))

    if user_move == secret:
        print("Угадали!")
        guessed = True
        break
    else:
        if user_move < secret:
            print("Неверно (загаданное число больше)")
        else:
            print("Неверно (загаданное число меньше)")
if not guessed:
    print(f"Попытки закончились. Правильный ответ: {secret}")