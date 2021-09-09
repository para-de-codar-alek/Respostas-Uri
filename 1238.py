n = int(input())

for l in range(n):
    start = input().split()
    a, b = start
    if len(b) >= len(a):
        c = ''
        for k in range(len(a)):
            c += a[k]+b[k] # pega a k-ésima substring de 'a' e soma com a de 'b' e vai add a 'c'
        c += b[len(a):] # Como o range só abrange o menor, adicionamos oq sobra da maior string a 'c'
        print(c)
    elif len(a) > len(b):
        c = ''
        for k in range(len(b)):
            c += a[k]+b[k]
        c += a[len(b):]
        print(c)