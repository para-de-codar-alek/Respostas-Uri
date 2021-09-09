n = int(input())

for l in range(n):
    c = ''
    phrase = input()

    for i in phrase:
        if (i.isalpha() == True):
            if i not in c:
                c+= i
    if len(c)<13:
        print('frase mal elaborada')

    elif len(c)>=13 and len(c)<26:
        print('frase quase completa')

    else:
        print ('frase completa')

