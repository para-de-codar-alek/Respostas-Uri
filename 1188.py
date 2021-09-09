init=[]
l = input()

for i in range(12):
    init.append([])
    for j in range(12):
        x = float(input())
        init[i].append(x)

w = 0
inf_num = 5
supporte = 7
cont = 0
for i in range(7,12):
    for j in range(inf_num,supporte):
        w += init[i][j]
        cont += 1
    inf_num -= 1
    supporte += 1

med = w / cont

if l == "S":
    print(f'{w:.1f}')
else:
    print(f'{med:.1f}')
