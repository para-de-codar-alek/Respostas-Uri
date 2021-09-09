qtd_test = int(input()) # Recebe o número de testes
i = 0

while i < qtd_test: # Executa os testes
    lista = [] # Lista, na qual as instruções irão ficar.
    pos = 0 # Indica a posição na qual o robô está
    #print(lista) 
    #print(pos)
    num_of_inst = int(input()) # Número de instruções que o robô vai receber nesse teste

    for l in range (num_of_inst):
        instruction =  list(map(str, input().split())) # Onde as instruções vão ser recebidas

        if instruction[0] == "LEFT": # Se a instrução for LEFT a pos recebe -1
            pos-=1
            lista.append(instruction)
            #i+=1
            #print(lista)

        elif instruction[0] == "RIGHT": # Se for Right recebe +1
            pos+=1
            lista.append(instruction)
            #print('OK')
            #i+=1

        else: # Condição para instrução SAME AS N
            if instruction[0]!=instruction[-1]:
                num = int(instruction[2])
                take_elem = lista[num-1]
                print(take_elem)
                lista.append(take_elem)
                #i+=1

                if take_elem == 'LEFT' or take_elem == "['LEFT']": # Condição para verificar se o elento de Same é L ou R
                    pos-=1
                    print('barracuda')

                else:
                    pos+=1
                    print('OK')
    #lista.clear()
    #lista = [0]                
    print(pos)    
    i+=1


