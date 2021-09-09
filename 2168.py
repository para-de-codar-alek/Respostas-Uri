

initial = int(input())
lista = []
for l in range(initial+1):
    value = input()
    value = value.split(' ')
    lista.append(value)

Counter = 0
for l in range(initial):
    for x in range(initial):
        if int(lista[l][x]) == 1:
            Counter += 1
        if int(lista[l][x+1]) == 1:
            Counter += 1
        if int(lista[l+1][x]) == 1:
            Counter += 1
        if int(lista[l+1][x+1]) == 1:
            Counter += 1

        if Counter < 2:
            print('U', end='')
        else:
            print('S', end='')

        Counter = 0
    print()

