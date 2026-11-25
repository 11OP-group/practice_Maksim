a,b,c = map(int, input().split())

if a + b > c or a + c > b or b + c > a:
    if a == b == c:
        print("Равносторонний")
    elif a == b or a == c or b == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
else:
    print("Не существует")