weight, height = map(float, input("Введите вес и рост через пробел: ").split())

bmi = weight / (height * height)

print(f"Ваш ИМТ: {bmi:.1f}")
