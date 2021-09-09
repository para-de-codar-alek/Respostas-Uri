n = int(input())

for l in range(n):
    piece = input().split()
    a, b = piece
    c =  ''   
    if len(b)>len(a):
        print('nao encaixa')
    elif len(a)>=len(b):
        c= a[::-1]
        test = c[:len(b)]
        test= test[::-1]
        if test == b:
            print('encaixa')
        else:
            print('nao encaixa')