n = int(input())
i = 0

while i<n:
    dictionarie = {}
    lista= []
    num_products = int(input())

    for l in range(num_products):
        products_price = tuple(input().split()) #Criando uma tupla que recebe dois valores em sua posição
        lista.append(products_price) #add as tupla a lista, para fazer uma lista de tuplas

    new_dict = dict(lista) # transformando a lista de tuplas em um dicionário
    dictionarie.update(new_dict) # Juntando o dicionário inicial com o dicionário da lista de tuplas
    bought_prod = int(input())
    s = 0

    for p in range(bought_prod):
        search_price = input().split() # var para procurar 1 a key do produto e 2 a qtd desse produto comprado
        search_prod, search_value = search_price 
        search_value = int(search_value) #transformando a qtd de produtos em inteiros


        price = dictionarie[search_prod] # buscando o valor da chave inserida em search prod
        price = float(price) # ^floatando esse valor, pois estava como string
        s+= price*search_value # somando os valor dos produtos adicionados e mult pela qtd.
    

    print(f'R$ {s:.2f}')
    i+=1
