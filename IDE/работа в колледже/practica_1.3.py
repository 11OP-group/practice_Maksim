maxi=0

while True:

    num=int(input("Введите число"))
    maxi=max(num,maxi)
    if num==0:
        print(maxi)
        break