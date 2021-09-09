

def asciii(words):
    frequency = {}
    for string in words:

        if not str(ord(string)) in frequency:
            frequency[str(ord(string))] = 1

            continue
        frequency[str(ord(string))] += 1

    return sorted({k: v for k, v in sorted(frequency.items(), key=lambda item: item[1])})


lista = list(frequency.items())
n = len(lista)

    for i in range(n):
        for j in range(n):

            if lista[i][1] == lista[j][1] and int(lista[j][0]) < int(lista[i][0]):            
                Counter = lista[i]
                lista[i] = lista[j]
                lista[j] = Counter
    return lista


while True:
    try:
            line = asciii(input())                       
            [print (f'{tupla[0]} {tupla[1]}') for tupla in line]
    except EOFError:
        break