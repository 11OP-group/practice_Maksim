import math

def calculate_distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

def calculate_triangle_area(a, b, c):
    semi_perimeter = (a + b + c) / 2
    return math.sqrt(
        semi_perimeter
        * (semi_perimeter - a)
        * (semi_perimeter - b)
        * (semi_perimeter - c)
    )

print("Введите координаты точки A (x y):")
ax, ay = map(float, input().split())

print("Введите координаты точки B (x y):")
bx, by = map(float, input().split())

print("Введите координаты точки C (x y):")
cx, cy = map(float, input().split())

side_ab = calculate_distance(ax, ay, bx, by)
side_bc = calculate_distance(bx, by, cx, cy)
side_ca = calculate_distance(cx, cy, ax, ay)

area = calculate_triangle_area(side_ab, side_bc, side_ca)

print(f"Сторона AB: {side_ab:.2f}")
print(f"Сторона BC: {side_bc:.2f}")
print(f"Сторона CA: {side_ca:.2f}")
print(f"Площадь треугольника: {area:.2f}")
