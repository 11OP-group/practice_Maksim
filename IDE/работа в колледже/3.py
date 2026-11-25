temperature = float(input("Введите температуру в цельсиях"))
pressure = int(input("Введите давление"))
pulse = int(input("Введите пульс"))

result = ""

if temperature < 35 or temperature > 38 or pressure < 105 or pressure > 140 or pulse < 55 or pulse > 110:
    result = "Врач"
elif 36 <= temperature <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    result = "Нормальное состояние"
else:
    print("Легкое недомогание")

print(result, f"Показатели: Температура = {temperature}, Давление = {pressure}, Пульс = {pulse}")
