n = int(input()) # Quantas linhas de entrada vai ter para o for
i = 0
m = 0
y = 0
lista = [0]
while i<=60: ## Usamos o while para obter todos os 60 elementos de fibonacci
    if m==0:
        m+=1
        i+=1
        lista.append(m) ## damos append neles em uma lista que será usada para encontrarmos o valor da pos desejada
    else:
        m = m+y
        y = m-y
        i+=1
        lista.append(m)

for j in range(n):
    n1 = int(input()) ## Digitamos a posição desejada e recebemos o número da sequência naquela posição
    print(f'Fib({n1}) = {lista[n1]}')
