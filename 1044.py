#Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem 
# "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
# A <-- valor 1, B <-- valor 2
# Se A//2 = 0 retorna são múltiplos, senão não são múltiplos
line = input().split()
A, B = line
if (int(A)%int(B) == 0 or int(B)%int(A) == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
