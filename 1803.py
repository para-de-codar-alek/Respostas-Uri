lista = []

for l in range(0,4):
    enter = list(map(str, input()))
    lista.append(enter)
   
vertical_list = []
for i in range(len(lista[0])):
    v_strings = lista[0][i]+lista[1][i]+lista[2][i]+lista[3][i]
    vertical_list.append(v_strings)

for x in range(len(vertical_list)):
    vertical_list[x] = int(vertical_list[x])
c = ''
for y in range(len(vertical_list)-2):
    decod = (vertical_list[0] * vertical_list[y+1] + vertical_list[-1]) % 257
    c+= chr(decod)

print(c)



