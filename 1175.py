# Ler um vetor N[20] e trocar os valores com os ultimos da lista-1
# até trocar 0 10 com 11,mostrar o novo vetor
lista = []
for l in range(20):
    N = int(input())
    lista.append(N)
    if l == 19:
        lista.reverse()
for j in range (20):
    print (f'N[{j}] = {lista[j]}')

