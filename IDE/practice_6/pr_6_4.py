MIN_CELL, MAX_CELL = 1, 8

col1, row1, col2, row2 = map(int, input("Введите столбец и строку 1-й клетки, затем 2-й: ").split())

if not (MIN_CELL <= col1 <= MAX_CELL and MIN_CELL <= row1 <= MAX_CELL and MIN_CELL <= col2 <= MAX_CELL and MIN_CELL <= row2 <= MAX_CELL):
    print("ошибка ввода")
else:
    same_diagonal = abs(col2 - col1) == abs(row2 - row1)
    print("YES" if same_diagonal else "NO")
