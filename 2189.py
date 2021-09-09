n = 1
i= 1
while n !=0:
    n = int(input())

    if n==0:
        i=0
        break

    else:
        inv = list(map (int, input (). split ()))
        inv.insert(0,0)
        print(f'Teste {i}')
        for l in range(1,n+1):
            if l == inv[l]:
                print(l)
                print()
    i+=1
    inv.clear()
