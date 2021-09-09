while True:
    try:
        c = ''
        p = 0
        matriz = []
        line = input().split()
        n, m = line
        n = int(n)
        m = int(m)

        for l in range(n):
            pos = list(map(int, input().split()))
            matriz.append(pos)
        for x in range (n):
            c = ''
            for y in range(m):
                p = 0
                if (matriz[x][y] == 1):
                    c+= '9'
                else:
                    if (x > 0 and matriz[x-1][y] == 1):
                        p+=1
                    if (x < len(matriz)-1) and matriz[x + 1][y] == 1:
                        p+=1
                    if (y > 0 and matriz[x][y-1] == 1):
                        p+=1
                    if (y < len(matriz[x])-1) and matriz[x][y+1] == 1:
                        p+=1
                    p = str(p)
                    c+=p
            print(c)
    except EOFError:
        break
