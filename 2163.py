l = input().split()
n_linha, n_coluna = int(l[0]), int(l[1])

n = list() 

for i in range(n_linha):                               
    n.append( [int(col_i) for col_i in input().split()] )  

teste = teste2 = 0
search = False

for i in range(1, n_linha-1):
    if search:
        break

    for j in range(1, n_coluna-1):
        if n[i][j] == 42:
            if n[i-1][j-1] == 7 and n[i-1][j] == 7 and n[i-1][j+1] == 7:
                if n[i][j-1] == 7 and n[i][j + 1] == 7:
                    if n[i+1][j-1] == 7 and n[i+1][j] == 7 and n[i+1][j+1] == 7:
                        teste = i+1
                        teste2 = j+1
                        search = True
                        break

print("{} {}".format(teste, teste2))