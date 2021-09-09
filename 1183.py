sodoku_list=[]
test = int(input())
for a in range(test) :
    test1=False
    matriz=[]
    for j in range(9) :
        matriz.append(list(map(int,input().split(" "))))
    for linha in matriz :
        for coluna in linha :
            if linha.count(coluna)>1 : test1=True
    for i in range(9) :
        x=[]
        for linha in matriz :
            if not(linha[i] in x) : x.append(linha[i])
        if len(x)!=9 :
            test1=True
    for linham in range(0,9,3) :
        element1=[]
        element2=[]
        element3=[]
        for linha in range(linham,linham+3) :
            for colunam in range(0,9,3) :
                for coluna in range(colunam,colunam+3) :
                    if colunam==0 :
                        if not(matriz[linha][coluna] in element1) : element1.append(matriz[linha][coluna])
                    if colunam==3 :
                        if not(matriz[linha][coluna] in element2) :  element2.append(matriz[linha][coluna])
                    if colunam==6 :
                        if not(matriz[linha][coluna] in element3) : element3.append(matriz[linha][coluna])
        if len (element2)!= 9 : test1= True
        if len(element3)!= 9 : test1= True
        if len(element1)!= 9 : test1= True
    sodoku_list.append([])
    sodoku_list[-1].append("Instancia " + str(a+1))
    if test1 : sodoku_list[-1].append("NAO")
    else : sodoku_list[-1].append("SIM")
for i in sodoku_list :
    print(i[0])
    print(i[1])
    print()