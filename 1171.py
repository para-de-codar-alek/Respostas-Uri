n1 = int(input())
lista = {}

for l in range (n1):
    N = int(input())
    if (N in lista):
        lista[N]+=1
    else:
        lista[N] = 1

key = lista.keys()
key = sorted(key)

for i in key:
    print (f'{i} aparece {lista[i]} vez(es)')