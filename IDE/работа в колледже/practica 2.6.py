user=input('введите слово для проверки: ')

chars=list(user)
reversed_chars = chars[::-1]

if chars == reversed_chars:
    print(f'Это палиндром: {chars}')
else:
    print(f'Это не палиндром: {chars}')