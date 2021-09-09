# Programa para verificar se há um pico após o vale ou assim sucessivamente
# a entrada tem uma linha que dirá o caso de testes e o a próxima com os casos de teste

N = int(input())
lista = [int(x) for x in input().split()]
peak = 0
if N == 2 and lista[0] == lista[1]:
    peak = 0

else:
    for l in range(1,N-1):
        if  lista[l-1]>lista[l] and lista[l]<lista[l+1] or lista[l-1]<lista[l] and lista[l]>lista[l+1]: #peak =1 ,  not ((h[i] < h[i-1] and h[i] < h[i+1]) or (h[i] > h[i-1] and h[i] > h[i+1])): peak =0 (prog que deu certo)
             peak = 1
             break
print (peak)
        
'''if  lista[l-1]>lista[l] and lista[l]<lista[l+1] or lista[l-1]<lista[l] and lista[l]>lista[l+1]:
             peak = 1
             break'''