
i = 1    
while i!=0:
    n = int(input())
    if n==0:
        i = 1
        break
    else:
        lista = []
        for l in range(n):
            name_ = input()
            lista.append(name_)
        max_ = max(lista, key=len)
        if i>1:
            print()
        for l in lista:

            if len(l)<len(max_):
                space = len(max_)-len(l)
                space = space * ' '
                just = space+l
                print(just)
            else:
                print(l)
    i+=1


