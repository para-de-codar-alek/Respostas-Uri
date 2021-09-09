# Um programa que leia valores em um intervalo inputado e nos mostre em ordem crescente os pares
# e depois o ímpares em decr
# Jogar os elementos divisíveis por 2 em uma lista e os não em outra
# logo após sort as listas e mostrar em um loop os elementos da par primeiro e da ímpar logo após

counter = int(input()) # Número de vezes que uma entrada vai ser inputada
pair = []
no_pair = []

for l in range (counter): # vezes que a entrada colocada em counter vai ser executada
    test_value = int(input()) # os inputs se pares são colocados na lista pair senão na lista no_pair

    if test_value % 2 == 0:
        pair.append(test_value)
    else:
        no_pair.append(test_value)

pair = sorted(pair) # ordenando a lista par 
no_pair = sorted(no_pair)
no_pair = no_pair[::-1] # invertendo a lista ímpar ordenada


for i in range(len(pair)):
    print (pair[i])

for j in range(len(no_pair)):
    print(no_pair[j])


