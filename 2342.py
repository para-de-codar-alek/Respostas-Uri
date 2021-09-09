max_value = int(input())
line = input().split()
v1,sign,v2 = line
if sign == '*':
    v1 = int(v1)
    v2 = int(v2)
    if v2*v1<=max_value:
        print('OK')
    else:
        print ('OVERFLOW')
elif sign == '+':
    v1 = int(v1)
    v2 = int(v2)
    if v1+v2<=max_value:
        print ('OK')
    else:
        print ('OVERFLOW')
    