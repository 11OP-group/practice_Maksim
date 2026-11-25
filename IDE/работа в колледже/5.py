x1,y1,x2,y2 = map(int,input("Введите 4 точки : ").split())

def checker (x,y):
    if (x + y) % 2 != 0:
        return "Цветная"
    else:
        return "Не цветная"



if checker(x1,y1) == "Цветная" and checker(x2,y2) == "Цветная" or checker(x1,y1) == "Не цветная" and checker(x2,y2) == "Не цветная":
    print("Обе покрашены в один цвет")
else:
    print("Разные цвета у клеток")

