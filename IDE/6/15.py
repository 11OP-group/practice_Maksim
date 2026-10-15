age=int(input('введите ваш возраст'))
document=input('есть ли документ(да/нет)')
member = input('есть ли карта клуба(да/нет)')

if (member == 'да') or (age >18 and document=='да'):
    print('Добро пожаловать')
else:
    print('Доступ запрещён')