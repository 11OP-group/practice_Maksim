PI = 3.141592653589793

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return PI * radius ** 2

rect_width, rect_height = map(float, input( "Введите ширину и высоту прямоугольника через пробел: ").split())
rect_area = calculate_rectangle_area(rect_width, rect_height)
print(f"Площадь прямоугольника: {rect_area:.2f}")

circle_radius = float(input("Введите радиус круга: "))
circle_area = calculate_circle_area(circle_radius)
print(f"Площадь круга: {circle_area:.2f}")
