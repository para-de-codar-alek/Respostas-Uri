# Dentre os valores inputados Theon será punido a quantidade de vezes o valor que estã na posição que ele escolheu
# Logo enontrar o menor valor e sua posição

entering = int(input()) # a qtd de valores que serão colocados em linha
line_value = input().split() # tupla para receber os valores

for l in range(entering): # repetição para colocar l números na tupla e fazêlos virarem números inteiros
    line_value[l] = int(line_value[l])

minimum = min(line_value) # acha o menor valor da tupla
print (f'{line_value.index(minimum)+ 1}') # acha a posição do menor valor da tupla
