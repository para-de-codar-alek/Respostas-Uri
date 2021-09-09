wifi_sign = input()
c = ''
for l in wifi_sign:
    if l == '1':
        c+= l
if len(c) % 2 == 0:
    wifi_sign = wifi_sign + '0'
    print (wifi_sign)
else:
    wifi_sign = wifi_sign + '1'
    print(wifi_sign)
    