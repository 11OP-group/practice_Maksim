IP=input()
octets=IP.split('.')

valid_count=0

for part in octets:
    if 0<=int(part)<=255:
        valid_count+=1

if len(octets)==4 and valid_count==4:
    print('YES')
else:
    print('NO')