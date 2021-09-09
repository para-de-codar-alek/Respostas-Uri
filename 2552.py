while True:
    try:
        line = input().split()
        n, m = line
        n = int(n)
        m = int(m)
        lista = list()
        for l in range(1,m+1):
            lista.append([l])
        for j in range(n):
            lista2 = list(map (int, input (). split ()))
            lista[j].append(lista2[:])
            lista2.clear()
        #print(lista)

        for x in range (m):
            print(x)
            #for y in range (n):
            print(lista[x][0])


    except EOFError:
        break