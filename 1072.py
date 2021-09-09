# Receber um Número N, e esse número vai ser a quantidade de vezes que valores serão recebidos em x
# depois verificar se os valores em x fazem parte do intervalo [10:20]
n = int(input())
dentro = 0
fora = 0

for l in range (0,n):
    value = int(input())
    if value<=20 and value>=10:
        dentro+=1
    else:
        fora+=1
print ('{} in'.format(dentro))
print ('{} out'.format(fora))