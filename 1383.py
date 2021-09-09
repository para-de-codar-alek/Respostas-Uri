vector =[]
test = int(input())
for a in range(test) :
    fake=False
    sudoku=[]
    for i in range(9) :
        sudoku.append(list(map(int,input().split(" "))))
    for linha in sudoku :
        for coluna in linha :
            if linha.count(coluna)>1 : fake=True
    for i in range(9) :
        x=[]
        for linha in sudoku :
            if not(linha[i] in x) : x.append(linha[i])
        if len(x)!=9 :
            fake=True
    for linham in range(0,9,3) :
        x1=[]
        x2=[]
        x3=[]
        for linha in range(linham,linham+3) :
            for colunam in range(0,9,3) :
                for coluna in range(colunam,colunam+3) :
                    if colunam==0 :
                        if not(sudoku[linha][coluna] in x1) : x1.append(sudoku[linha][coluna])
                    if colunam==3 :
                        if not(sudoku[linha][coluna] in x2) : x2.append(sudoku[linha][coluna])
                    if colunam==6 :
                        if not(sudoku[linha][coluna] in x3) : x3.append(sudoku[linha][coluna])
        if len(x2)!=9 : fake=True
        if len(x3)!=9 : fake=True
        if len(x1)!=9 : fake=True
    vector .append([])
    vector [-1].append("Instancia " + str(a+1))
    if fake : vector [-1].append("NAO")
    else : vector [-1].append("SIM")
for i in vector  :
    print(i[0])
    print(i[1])
    print()