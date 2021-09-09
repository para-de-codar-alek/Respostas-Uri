dicionario = {}
test = int(input())
i = 0

while i<test:
    
    n = int(input())

    for l in range(n):
        lista_name = list(map(str, input().split()))
        lista_freq = list(map(str, input().split()))
        print(lista_name)
        print(lista_freq)
    w = 0
    print(len(lista_name))
    while w<len(lista_name):
        dicionario[lista_name[w]] = lista_freq[w]
        w+=1
    print(dicionario)

    for l in range (len(lista_name)):
        counter = 0
        


