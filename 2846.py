i = 0
m = 0
y = 0
lista = [] 
lista2 = []
K = int(input())
if K<6:
    while i<6:
        if m==0:
            m+=1
            i+=1
            lista.append(0)
            lista.append(m)
        else:
            m = m+y
            y = m-y
            i+=1
            lista.append(m)
else:
    while i<K:
        if m==0:
            m+=1
            i+=1

            lista.append(0)
            lista.append(m)
        else:
            m = m+y
            y = m-y
            i+=1
            lista.append(m)
lista2.append(0)
for l in range (m):
    if l not in lista:
        lista2.append(l)

print(lista2[K])






