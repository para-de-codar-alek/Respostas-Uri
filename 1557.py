n = 99999
while True:
    n = int(input())
    if n == 0:
        break
    
    lista = list()
        
    for i in range(n):
        lista.append([])
        for j in range(n):
            lista[i].append(0)
    lista[0][0] = 1
    print(lista)

    for l in range(0,n):
        if i>=1:
            lista[l][0] = lista[l-1][0]*2
    value = len(str(lista[n-1][n-1]))
    for i in range(n):
        for j in range(n):
            lista[i][j] = str(lista[i][j])
            while len(lista[i][j]) < value:
                lista[i][j] = ' ' + lista[i][j]
        lista = ' '.join(lista[i])

        print(lista)
        print()